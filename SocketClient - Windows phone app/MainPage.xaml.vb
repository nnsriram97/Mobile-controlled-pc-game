' The Blank Application template is documented at http://go.microsoft.com/fwlink/?LinkID=391641

Imports Windows.Networking.Sockets
Imports Windows.Networking
Imports Windows.Storage.Streams
Imports Windows.Devices.Sensors
Imports Windows.Storage

''' <summary>
''' An empty page that can be used on its own or navigated to within a Frame.
''' </summary>
Public NotInheritable Class MainPage
	Inherits Page

	Private clientSocket As StreamSocket
	Dim writer As DataWriter
	Private serverHost As HostName
	Private serverHostNameString As String
	Private serverPort As String
	Private connected As Boolean = False

	Private acc As Accelerometer

	''' <summary>
	''' Invoked when this page is about to be displayed in a Frame.
	''' </summary>
	''' <param name="e">Event data that describes how this page was reached.
	''' This parameter is typically used to configure the page.</param>
	Protected Overrides Sub OnNavigatedTo(e As Navigation.NavigationEventArgs)
		' TODO: Prepare the page for display here.

		' TODO: If your application contains multiple pages, ensure that you are
		' handling the hardware Back button by registering for the
		' Windows.Phone.UI.Input.HardwareButtons.BackPressed event.
		' If you are using the NavigationHelper provided by some templates,
		' this event is handled for you.
		DisplayInformation.AutoRotationPreferences = DisplayOrientations.Landscape Or DisplayOrientations.LandscapeFlipped
		Frame.BackStack.Clear()
	End Sub

	Public Sub New()

		' This call is required by the designer.
		InitializeComponent()
		' Add any initialization after the InitializeComponent() call.
		acc = Accelerometer.GetDefault
		Dim settings = ApplicationData.Current.LocalSettings
		If acc IsNot Nothing Then
			If settings.Values.ContainsKey("Interval") And acc.MinimumReportInterval < Convert.ToUInt32(settings.Values("Interval")) Then
				acc.ReportInterval = 30
			Else
				acc.ReportInterval = acc.MinimumReportInterval
			End If
			AddHandler acc.ReadingChanged, New TypedEventHandler(Of Accelerometer, AccelerometerReadingChangedEventArgs)(AddressOf ReadingChanged)
			writer = New DataWriter(App.clientsocket.OutputStream)
		End If
	End Sub

	Private Async Sub ReadingChanged(sender As Object, e As AccelerometerReadingChangedEventArgs)
		Await Dispatcher.RunAsync(Windows.UI.Core.CoreDispatcherPriority.Normal, Async Sub()
																						   Dim reading As AccelerometerReading = e.Reading
																						   AccValues.Text = String.Format("{0:0.00}", reading.AccelerationX * 10) & "," & String.Format("{0:0.00}", reading.AccelerationY * 10) & "," & String.Format("{0:0.00}", reading.AccelerationZ * 10) & "-" & ButtonA.IsPressed & " " & ButtonB.IsPressed
																						   'If connected Then
																						   Try
																							   Dim data = String.Format("{0:0.00} {1:0.00} {2:0.00} {3} {4}", reading.AccelerationX * 10, reading.AccelerationY * 10, reading.AccelerationZ * 10, Convert.ToInt32(ButtonA.IsPressed), Convert.ToInt32(ButtonB.IsPressed))

																							   writer.WriteString(data)
																							   Await writer.StoreAsync()
																							   'writer.DetachStream()
																							   'writer.Dispose()
																						   Catch ex As Exception
																							   Debug.WriteLine(ex.Message)
																						   End Try
																						   'End If
																					   End Sub)
	End Sub
End Class