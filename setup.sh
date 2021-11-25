mkdir -p ~/.streamlit/

echo "[theme]
    primaryColor = ‘#84a3a7’
    backgroundColor = ‘#EFEDE8’
    secondaryBackgroundColor = ‘#fafafa’
    textColor= ‘#424242’
    font = ‘sans serif’
    [server]
    headless = true
    port = $PORT
    enableCORS = false
" > ~/.streamlit/config.toml

echo "\                                                                         
    [server]\n\                                                                     
    port = $PORT\n\                                                                 
    enableCORS = false\n\                                                           
    headless = true\n\                                                              
    \n\                                                                             
" > ~/.streamlit/config.toml
