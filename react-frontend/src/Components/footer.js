import React, { Component } from 'react';
import {
    Box
} from '@material-ui/core';

class Footer extends Component {
    render() {
        return (
            <Box style={{
                bottom: 0,
                paddingBottom: '1em',
                paddingTop: '1em',
                background: 'lightgrey',
                textAlign: 'center'
            }}>
                <Box>
                    &copy; 2022, Ayush Jain
                </Box>
            </Box>
        );
    }
}

export default Footer;