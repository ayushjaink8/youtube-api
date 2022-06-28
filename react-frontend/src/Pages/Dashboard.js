import React, { useEffect, useState } from 'react';
import Footer from '../Components/footer';
import Header from '../Components/header';
import { Alert } from '@mui/material';

import Pagination from '@mui/material/Pagination';

import {
    Box, Button, Switch, Typography
} from '@material-ui/core';

import {
    sleep,
    getYoutubeData,
    refreshYoutubeFeeds
} from '../Services/data'
import DataTable from '../Components/DataTable';

function Dashboard() {
    
    const [Videos, setVideos] = useState([]);
    const [Count, setCount] = useState(0);
    const [Toggle, setToggle] = useState(false);
    const [Page, setPage] = useState(1);
    const [ShowAlert, setShowAlert] = useState(false);

    const func = async (page) => {
        const result = await getYoutubeData(page);
        setVideos(result.results);
        setCount(result.count);
    }

    useEffect(() => {
        func(Page);
    }, [Page])

    useEffect(() => {
        refresh();
    }, [Toggle])
    useEffect(()=>{
        setTimeout(() => {
            setShowAlert(false);
         }, 2000)       
    }, [ShowAlert])

    function getToggleValue(){
        return Toggle;
    }

    const refresh = async () => {
        let knob = getToggleValue();
        while (knob) {
            await refreshYoutubeFeeds();
            await func(Page);
            await sleep(10000);
            setShowAlert(true);
            knob = getToggleValue();
        }
    }

    const OnRefresh = async (e) => {
        await refreshYoutubeFeeds();
        await func(Page);
        setShowAlert(true);
    }

    const handleChange = async (e) => {
        setToggle(e.target.checked);
    };

    const handlePagination = async (event, value) => {
        setPage(value);
    }
    
    return (
        <Box style={{height: '100vh', textAlign: 'left'}}>
            <Header/>
            <Box>
                <Box>
                    {ShowAlert ? <Alert severity="success">Content refreshed Successfully!</Alert> : <></>}
                </Box>
                <Box style={{margin: '3em'}}>
                    Total Youtube Data Count: {Count}
                    <Box style={{display: 'inline', marginLeft: '3em'}}>
                        <Button variant="contained" color="primary" onClick={OnRefresh}> Refresh </Button>
                    </Box>
                </Box>
                <Box style={{margin: '3em'}}>
                    Refresh asynchronously after every 10 seconds
                    <Box style={{display: 'inline', marginLeft: '1em'}}>
                        <Switch checked={Toggle} color="primary" onChange={handleChange} />
                    </Box>
                </Box>
                <Box style={{margin: '3em', textAlign: 'center'}}>
                    <Typography variant="h4" component="h2"> Data Table </Typography> 
                    <Box style={{margin: '2em'}}>
                        <DataTable Videos={Videos}/>
                    </Box>
                    <Box style={{margin: '2em', display: 'flex', placeContent: 'center'}}>
                        <Pagination
                            count={Math.ceil(Count/10)}
                            page={Page} variant="outlined"
                            color="primary"
                            onChange={handlePagination}/>
                    </Box>
                </Box>
            </Box>
            <Footer/>
        </Box>
    );
}

export default Dashboard;