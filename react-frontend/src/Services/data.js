import React from 'react';
import axios from 'axios';

const base_url = 'http://127.0.0.1:8000';

const sleep = (milliseconds) => {
    return new Promise(resolve => setTimeout(resolve, milliseconds))
}

async function getYoutubeData(page) {
    try{
        const data = await axios.get(base_url + '/yt/?page=' + page.toString());
        return data.data;
    } catch (err) {
        console.log(err);
        return {};
    }
};

async function refreshYoutubeFeeds() {
    try{
        const data = await axios.get(base_url + '/refresh');
        return data;
    } catch (err) {
        console.log(err);
        return {};
    }
};

export {
    sleep,
    getYoutubeData,
    refreshYoutubeFeeds
};