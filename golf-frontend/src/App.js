import React, {useState} from "react";
import useSWR from "swr";
import { TableVirtuoso } from 'react-virtuoso'
import Table from '@mui/material/Table'
import TableBody from '@mui/material/TableBody'
import TableCell from '@mui/material/TableCell'
import TableContainer from '@mui/material/TableContainer'
import TableHead from '@mui/material/TableHead'
import TableRow from '@mui/material/TableRow'
import Paper from '@mui/material/Paper'

// const TableComponents = {
//   Scroller: React.forwardRef((props, ref) => <TableContainer component={Paper} {...props} ref={ref} />),
//   Table: (props) => <Table {...props} style={{ borderCollapse: 'separate' }} />,
//   TableHead: TableHead,
//   TableRow: TableRow,
//   TableBody: React.forwardRef((props, ref) => <TableBody {...props} ref={ref} />),
// }

// const fetcher = (url) => fetch(url).then((res) => res.json());

// export default function App() {
//   const { data, error, isLoading } = useSWR(
//     "http://3.141.192.107/get-pga-best-odds",
//     fetcher
//   );

//   if (error) return "An error has occurred.";
//   if (isLoading) return "Loading...";
//   return (
//     <div>
//       <h1>Golf Elo</h1>
//       <p>Check out the best available odds</p>
//       <p> data</p>
      
//       {/* <TableVirtuoso
//         style={{ height: 400 }}
//         data={generateUsers(100)}
//         components={TableComponents}
//         fixedHeaderContent={() => (
//           <TableRow>
//             <TableCell style={{ width: 150, background: 'white' }}>
//               Name
//             </TableCell>
//             <TableCell style={{ background: 'white' }}>
//               Description
//             </TableCell>
//           </TableRow>
//         )}
//       itemContent={(index, user) => (
//           <>
//             <TableCell style={{ width: 150, background: 'white' }}>
//               {user.name}
//             </TableCell>
//             <TableCell style={{ background: 'white'  }}>
//               {user.description}
//             </TableCell>
//           </>
//         )}
//       /> */}
//     </div>
//   );
// }
export default function App() {
  const [data, setData] = useState(null);

  function handleClick() {
    const xhr = new XMLHttpRequest();
    xhr.open('GET', 'http://3.141.192.107/get-pga-best-odds');
    xhr.onload = function() {
      if (xhr.status === 200) {
        setData(JSON.parse(xhr.responseText));
      }
    };
    xhr.send();
  }

  return (
    <div>
      <button onClick={handleClick}>Get Data</button>
      {data ? <div>{JSON.stringify(data)}</div> : <div>Loading...</div>}
    </div>
  );
}