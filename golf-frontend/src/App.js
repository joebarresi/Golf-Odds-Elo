import React from "react";
import useSWR from "swr";
import { TableVirtuoso } from 'react-virtuoso'
import Table from '@mui/material/Table'
import TableBody from '@mui/material/TableBody'
import TableCell from '@mui/material/TableCell'
import TableContainer from '@mui/material/TableContainer'
import TableHead from '@mui/material/TableHead'
import TableRow from '@mui/material/TableRow'
import Paper from '@mui/material/Paper'

const TableComponents = {
  Scroller: React.forwardRef((props, ref) => <TableContainer component={Paper} {...props} ref={ref} />),
  Table: (props) => <Table {...props} style={{ borderCollapse: 'separate' }} />,
  TableHead: TableHead,
  TableRow: TableRow,
  TableBody: React.forwardRef((props, ref) => <TableBody {...props} ref={ref} />),
}

const fetcher = (url) => fetch(url).then((res) => res.json());

export default function App() {
  const { data, error, isLoading } = useSWR(
    "https://api.github.com/repos/vercel/swr",
    fetcher
  );

  if (error) return "An error has occurred.";
  if (isLoading) return "Loading...";
  return (
    <div>
      <h1>Golf Elo</h1>
      <p>Check out the best available odds</p>
      
      {/* <TableVirtuoso
        style={{ height: 400 }}
        data={generateUsers(100)}
        components={TableComponents}
        fixedHeaderContent={() => (
          <TableRow>
            <TableCell style={{ width: 150, background: 'white' }}>
              Name
            </TableCell>
            <TableCell style={{ background: 'white' }}>
              Description
            </TableCell>
          </TableRow>
        )}
      itemContent={(index, user) => (
          <>
            <TableCell style={{ width: 150, background: 'white' }}>
              {user.name}
            </TableCell>
            <TableCell style={{ background: 'white'  }}>
              {user.description}
            </TableCell>
          </>
        )}
      /> */}
    </div>
  );
}
