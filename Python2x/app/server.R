library(shiny)
library(rPython)

# set max upload limit to 100MB
options(shiny.maxRequestSize=2048*(1024**2))

shinyServer(function(input, output) {

  ## LOAD PYTHON
  #python.load('FIATestRun11.py')

  infileInfo <- reactive({
    print(input$FIA_batch_reporting_infile$name)
    print(input$FIA_batch_reporting_infile$size)
    print(input$FIA_batch_reporting_infile$type)
    print(input$FIA_batch_reporting_infile$datapath)
  })

## User options
  output$FIA_batch_reporting_user_options <- renderUI({
    validate(need(!is.null(input$FIA_batch_reporting_infile$datapath), ''))

    column(
      12,
      textInput('FIA_batch_reporting_outfileName',label = 'FIA Batch Reporting Output Filename', value = 'FIA_batch_reporting_Output_file' ))
  })

## Downloader
  output$FIA_batch_reporting_downloader <- renderUI({
    validate(need(!is.null(input$FIA_batch_reporting_infile$datapath), ''))

    list(
      downloadButton('FIA_batch_reporting_downloadMatchTypes', label = 'Download Bacth Reporting Export File')
      )
  })

## Download handler 
  output$FIA_batch_reporting_downloadMatchTypes <- downloadHandler(
    filename = function() {
      paste0(input$FIA_batch_reporting_outfileName, '.xlsx')
    },
    content = function(file) {
      ## TODO: Neeed to have a main function that has this method name in the main python file
      python.call( 'generate_bacth_reports', input$FIA_batch_reporting_infile$datapath, file)
    }
  )
})
