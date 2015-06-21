' The Blank Page item template is documented at http://go.microsoft.com/fwlink/?LinkID=390556
Imports Windows.Storage
Imports Windows.Networking.Sockets
Imports Windows.Networking
Imports Windows.UI.Popups

''' <summary>
''' An empty page that can be used on its own or navigated to within a Frame.
''' </summary>
Public NotInheritable Class ConnectPage
	Inherits Page
	Dim settings As ApplicationDataContainer = ApplicationData.Current.LocalSettings
	''' <summary>
	''' Invoked when this page is about to be displayed in a Frame.
	''' </summary>
	''' <param name="e">Event data that describes how this page was reached.
	''' This parameter is typically used to configure the page.</param>
	Protected Overrides Sub OnNavigatedTo(e As NavigationEventArgs)
		' TODO: Prepare page for display here.
		If settings.Values.ContainsKey("IP") Then
			IPText.Text = settings.Values("IP")
		End If
		If settings.Values.ContainsKey("Port") Then
			PortText.Text = settings.Values("Port")
		End If
		If settings.Values.ContainsKey("Interval") Then
			IntervalText.Text = settings.Values("Interval")
		End If
	End Sub

	Private Async Sub ConnectButton_Click(sender As Object, e As RoutedEventArgs)
		Try
			App.clientsocket = New StreamSocket
			Await App.clientsocket.ConnectAsync(New HostName(IPText.Text), PortText.Text)
			If settings.Values.ContainsKey("IP") Then
				settings.Values.Remove("IP")
			End If
			settings.Values.Add("IP", IPText.Text)
			If settings.Values.ContainsKey("Port") Then
				settings.Values.Remove("Port")
			End If
			settings.Values.Add("Port", PortText.Text)
			If settings.Values.ContainsKey("Interval") Then
				settings.Values.Remove("Interval")
			End If
			settings.Values.Add("Interval", IntervalText.Text)
			Frame.Navigate(GetType(MainPage))
		Catch ex As Exception
			Dim msg As MessageDialog
			msg.Content = "Cannot Connect"
			msg.ShowAsync()
		End Try
	End Sub
End Class
