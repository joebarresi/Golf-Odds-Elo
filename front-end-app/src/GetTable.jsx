import React, { useEffect, useState, setResults } from "react"
import { Fragment } from "react";

const URL = 'http://3.141.192.107/get-pga-best-odds'

function GetTable() {
    const [table, setTable] = useState([{Name: '',
                                      Odds: '',
                                      Book: ''}]);

    const fetchTable = async (url) => {
      try {
          const res = await fetch(url);
          const data = await res.json();
          if (data.info.length > 0) {
              setTable(data.info);
          }
          console.log(data.info);
          console.log("Received")
          // console.log(typeof(data))
      } catch (e) {
          console.error(e)
      }
    }

    useEffect(() => {
        fetchTable(URL);
    }, [])
   //const table = require("./test.json")

    return (
        <table class="styled-table">
        <thead>
        <tr>
           <th>
              <div>Golfer</div>
           </th>
           <th>
              <div>Odds</div>
           </th>
           <th>
              <div>Implied Probability</div>
           </th>
           <th>
              <div>Sportsbook</div>
           </th>
        </tr>
        {/* <tr class="table-module--header_row--1JSoq">
           <th colspan="1" aria-label="spacing"></th>
           <th>
              <button type="button" class="table-module--sortButton--2F9yG">
                 <div class="cell_styles-module--column_header_wrapper--1cLEK">
                    <div class="cell_styles-module--column_header_inner--31f15" data-active="false">
                       <p class="cell_styles-module--column_header_p--D5ka_">nfelo </p>
                    </div>
                 </div>
              </button>
           </th>
           <th>
              <button type="button" class="table-module--sortButton--2F9yG">
                 <div class="cell_styles-module--column_header_wrapper--1cLEK">
                    <div class="cell_styles-module--column_header_inner--31f15" data-active="false">
                       <p class="cell_styles-module--column_header_p--D5ka_">QB Adj </p>
                    </div>
                 </div>
              </button>
           </th>
           <th>
              <button type="button" class="table-module--sortButton--2F9yG">
                 <div class="cell_styles-module--column_header_wrapper--1cLEK">
                    <div class="cell_styles-module--column_header_inner--31f15" data-active="false">
                       <p class="cell_styles-module--column_header_p--D5ka_">Spread Value </p>
                    </div>
                 </div>
              </button>
           </th>
           <th>
              <button type="button" class="table-module--sortButton--2F9yG">
                 <div class="cell_styles-module--column_header_wrapper--1cLEK">
                    <div class="cell_styles-module--column_header_inner--31f15" data-active="false">
                       <p class="cell_styles-module--column_header_p--D5ka_">WoW </p>
                    </div>
                 </div>
              </button>
           </th>
           <th>
              <button type="button" class="table-module--sortButton--2F9yG">
                 <div class="cell_styles-module--column_header_wrapper--1cLEK">
                    <div class="cell_styles-module--column_header_inner--31f15" data-active="false">
                       <p class="cell_styles-module--column_header_p--D5ka_">YTD </p>
                    </div>
                 </div>
              </button>
           </th>
           <th>
              <button type="button" class="table-module--sortButton--2F9yG">
                 <div class="cell_styles-module--column_header_wrapper--1cLEK">
                    <div class="cell_styles-module--column_header_inner--31f15" data-active="false">
                       <p class="cell_styles-module--column_header_p--D5ka_">Actual </p>
                    </div>
                 </div>
              </button>
           </th>
           <th>
              <button type="button" class="table-module--sortButton--2F9yG">
                 <div class="cell_styles-module--column_header_wrapper--1cLEK">
                    <div class="cell_styles-module--column_header_inner--31f15" data-active="false">
                       <p class="cell_styles-module--column_header_p--D5ka_">Pythag </p>
                    </div>
                 </div>
              </button>
           </th>
           <th>
              <button type="button" class="table-module--sortButton--2F9yG">
                 <div class="cell_styles-module--column_header_wrapper--1cLEK">
                    <div class="cell_styles-module--column_header_inner--31f15" data-active="false">
                       <p class="cell_styles-module--column_header_p--D5ka_">PFF </p>
                    </div>
                 </div>
              </button>
           </th>
           <th>
              <button type="button" class="table-module--sortButton--2F9yG">
                 <div class="cell_styles-module--column_header_wrapper--1cLEK">
                    <div class="cell_styles-module--column_header_inner--31f15" data-active="false">
                       <p class="cell_styles-module--column_header_p--D5ka_">538 </p>
                    </div>
                 </div>
              </button>
           </th>
           <th>
              <button type="button" class="table-module--sortButton--2F9yG">
                 <div class="cell_styles-module--column_header_wrapper--1cLEK">
                    <div class="cell_styles-module--column_header_inner--31f15" data-active="false">
                       <p class="cell_styles-module--column_header_p--D5ka_">For </p>
                    </div>
                 </div>
              </button>
           </th>
           <th>
              <button type="button" class="table-module--sortButton--2F9yG">
                 <div class="cell_styles-module--column_header_wrapper--1cLEK">
                    <div class="cell_styles-module--column_header_inner--31f15" data-active="false">
                       <p class="cell_styles-module--column_header_p--D5ka_">Against </p>
                    </div>
                 </div>
              </button>
           </th>
           <th>
              <button type="button" class="table-module--sortButton--2F9yG">
                 <div class="cell_styles-module--column_header_wrapper--1cLEK">
                    <div class="cell_styles-module--column_header_inner--31f15" data-active="false">
                       <p class="cell_styles-module--column_header_p--D5ka_">Net </p>
                    </div>
                 </div>
              </button>
           </th>
           <th>
              <button type="button" class="table-module--sortButton--2F9yG">
                 <div class="cell_styles-module--column_header_wrapper--1cLEK">
                    <div class="cell_styles-module--column_header_inner--31f15" data-active="false">
                       <p class="cell_styles-module--column_header_p--D5ka_">/ Play </p>
                    </div>
                 </div>
              </button>
           </th>
           <th>
              <button type="button" class="table-module--sortButton--2F9yG">
                 <div class="cell_styles-module--column_header_wrapper--1cLEK">
                    <div class="cell_styles-module--column_header_inner--31f15" data-active="false">
                       <p class="cell_styles-module--column_header_p--D5ka_">/ Pass </p>
                    </div>
                 </div>
              </button>
           </th>
           <th>
              <button type="button" class="table-module--sortButton--2F9yG">
                 <div class="cell_styles-module--column_header_wrapper--1cLEK">
                    <div class="cell_styles-module--column_header_inner--31f15" data-active="false">
                       <p class="cell_styles-module--column_header_p--D5ka_">/ Rush </p>
                    </div>
                 </div>
              </button>
           </th>
           <th>
              <button type="button" class="table-module--sortButton--2F9yG">
                 <div class="cell_styles-module--column_header_wrapper--1cLEK">
                    <div class="cell_styles-module--column_header_inner--31f15" data-active="false">
                       <p class="cell_styles-module--column_header_p--D5ka_">/ Play </p>
                    </div>
                 </div>
              </button>
           </th>
           <th>
              <button type="button" class="table-module--sortButton--2F9yG">
                 <div class="cell_styles-module--column_header_wrapper--1cLEK">
                    <div class="cell_styles-module--column_header_inner--31f15" data-active="false">
                       <p class="cell_styles-module--column_header_p--D5ka_">/ Pass </p>
                    </div>
                 </div>
              </button>
           </th>
           <th>
              <button type="button" class="table-module--sortButton--2F9yG">
                 <div class="cell_styles-module--column_header_wrapper--1cLEK">
                    <div class="cell_styles-module--column_header_inner--31f15" data-active="false">
                       <p class="cell_styles-module--column_header_p--D5ka_">/ Rush </p>
                    </div>
                 </div>
              </button>
           </th>
           <th>
              <button type="button" class="table-module--sortButton--2F9yG">
                 <div class="cell_styles-module--column_header_wrapper--1cLEK">
                    <div class="cell_styles-module--column_header_inner--31f15" data-active="false">
                       <p class="cell_styles-module--column_header_p--D5ka_">/ Play </p>
                    </div>
                 </div>
              </button>
           </th>
        </tr> */}
     </thead>
     <tbody>
        {table.map((entry, i) => {
            return (
        <Fragment>
        <tr>
           {/* <td>
              <a class="cell_styles-module--linkOuter--3WtP5" href="/teams/kc/2023">
                 <div class="cell_styles-module--linkInner--2MNnD">
                    <div class="plate_styles-module--teamPlateContainer--2mDcV">
                       <div class="plate_styles-module--teamPlateIndex--27Ifn">1</div>
                       <div class="plate_styles-module--teamPlateLogoContainer--2kVIT" style="background: rgb(250, 216, 221);"><img class="plate_styles-module--teamPlateLogo--2gxru" src="https://a.espncdn.com/i/teamlogos/nfl/500/kc.png" alt="Chiefs logo"></div>
                       <div class="plate_styles-module--teamName--3mS-I">Chiefs</div>
                       <div class="plate_styles-module--teamNameMobile--N3TEQ">KC</div>
                    </div>
                 </div>
              </a>
           </td> */}
           <td>
                <div class="cell_styles-module--linkInner--2MNnD">
                <div>{entry.Name}</div>
                </div>
           </td>
           <td>
                <div class="cell_styles-module--linkInner--2MNnD">
                <div>{entry.Odds}</div>
                </div>
           </td>
           <td>
                <div class="cell_styles-module--linkInner--2MNnD">
                <div>{(entry.Odds > 0 ? (100/(entry.Odds + 100)*100) : entry.Odds/(entry.Odds+100)*100).toFixed(2) + '%'}</div>
                </div>
           </td>
           <td>
                <div class="cell_styles-module--linkInner--2MNnD">
                <div>{entry.Book}</div>
                </div>
           </td>
           
        </tr>
        </Fragment>
        );
    })}
    </tbody>
    </table>
    )
}

export default GetTable