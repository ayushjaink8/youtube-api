import * as React from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';
import { Link } from '@material-ui/core';

export default function DataTable({Videos}) {
  return (
    <TableContainer component={Paper}>
      <Table sx={{ minWidth: 650 }} aria-label="simple table">
        <TableHead>
          <TableRow>
            <TableCell><b>Video Title</b></TableCell>
            <TableCell align="right"><b>Channel Title</b></TableCell>
            <TableCell align="right"><b>Published DateTime</b></TableCell>
            <TableCell align="right"><b>Video Link</b></TableCell>
            <TableCell align="right"><b>Thumbnail Link</b></TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {Videos?.map((video, id) => (
            <TableRow
              key={id}
              id={id}
              sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
            >
              <TableCell component="th" scope="row">
                {video.video_title}
              </TableCell>
              <TableCell align="right">{video.channel_title}</TableCell>
              <TableCell align="right">{video.published_datetime}</TableCell>
              <TableCell align="right"><Link href={'https://www.youtube.com/watch?v=' + (video.url).split("/")[4]}>Link</Link></TableCell>
              <TableCell align="right"><Link href={video.thumbnail_url}>Link</Link></TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
}