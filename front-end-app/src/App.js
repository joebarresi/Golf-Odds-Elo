import GetTable from './GetTable'
import './App.css'


const App = () =>  {
  return (
    <div>
      <div tabindex="-1" >
        <div class="layout-module--app_background--3UQUD">
          <header class="header-module--box--3Od3_" data-active="false">
          <div class="header-module--constrainer--1g1jw">
            <div class="header-module--logoBox--1kMp5">
              <a class="header-module--logoLink--3c6Wv" href="/">
                <h3 class="header-module--logoText--noKFE">SharpGolf</h3>
              </a>
            </div>
            <div class="nav_cta-module--container--3XdfL" data-value="Mobile">
              <a class="nav_button-module--navLinkWrapper--2cuq4" href="/games/">
                <div class="nav_button-module--navContainer--3w_S5">
                  <p class="nav_button-module--navTitle--1tIf4">Games</p>
                </div>
              </a>
              <a aria-current="page" class="nav_button-module--navLinkWrapper--2cuq4 nav_button-module--navLinkWrapperActive--GnepH" href="/nfl-power-ratings/">
                <div class="nav_button-module--navContainer--3w_S5">
                  <p class="nav_button-module--navTitle--1tIf4">Teams</p>
                </div>
              </a>
              <a class="nav_button-module--navLinkWrapper--2cuq4" href="/qb-rankings/">
                <div class="nav_button-module--navContainer--3w_S5">
                  <p class="nav_button-module--navTitle--1tIf4">QBs</p>
                </div>
              </a>
              <a class="nav_button-module--navLinkWrapper--2cuq4" href="/analysis/">
                <div class="nav_button-module--navContainer--3w_S5">
                  <p class="nav_button-module--navTitle--1tIf4">Analysis</p>
                </div>
              </a>
            </div>
            </div>
            </header>
          </div>
          <div class="layout-module--app_container--u89un">
              <div class="layout-module--app_main--1WSwg">
                <div class="layout-module--app_body--32W21">
                  <div>
                    <div class="page_titles-module--title_div--15SVN">
                      <h2 class="page_titles-module--title_h2--1CX1o">Live Odds and Stats</h2>
                      <h3 class="page_titles-module--title_h3--2AxiE">Live Odds Scraped from Various Books</h3>
                  </div>
                    {/* <div class="top_bar-module--topBar--1ubPN">
                      <a download="nfelo-power-rankings.csv" class="csvDownload-module--csvLink--gA2TL" target="_self" href="blob:https://www.nfeloapp.com/2f9d6ebf-ec73-45d9-9d69-3892483b625b">
                        <div class="csvDownload-module--downloadButton--_uEfy">Download <span class="csvDownload-module--iconSpan--hYLYw">⎘</span>
                        </div>
                      </a>
                    </div> */}
                    <div>
                      <GetTable/>
                    </div>
                </div>
              </div>
          </div>  
      </div>
    </div>
  </div>
  );

}

export default App;