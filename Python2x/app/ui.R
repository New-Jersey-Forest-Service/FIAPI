library(shiny)

shinyUI(
	fluidPage(

		tags$div(align='center',

			titlePanel(title = 'PyEVALIDator Batch Reporting'),
			sidebarLayout(position = "left",
				sidebarPanel("Make sure the file being uploaded is formatted correctly"),
				mainPanel()),

			fluidRow(
				column(4),
				column(4,
					fileInput(inputId = 'FIA_batch_reporting_infile',multiple = FALSE, label = 'Upload Bacth Reporting File (Max 100MB)')),
				column(4)),
			br(),
			fluidRow(
				column(8),
				column(8,
					uiOutput('FIA_batch_reporting_user_options')),
				column(8,
					uiOutput('FIA_batch_reporting_downloader')),
				column(8))
			)
		)
  )
