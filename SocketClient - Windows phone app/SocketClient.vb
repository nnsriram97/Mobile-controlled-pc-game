Imports Windows.Networking.Sockets
Imports System.Threading
Imports System.Text

Public Class SocketClient
	Dim socket As StreamSocket = Nothing
	Shared clientDone As ManualResetEvent = New ManualResetEvent(False)
	ReadOnly Timeout_millis As Integer = 5000
	ReadOnly Max_Buffer_Size As Integer = 2048

	Public Function Connect(ByVal hostName As String, ByVal portNumber As Integer) As String
		Dim result As String = String.Empty

		'		Dim hostEntry As Windows.Networking.EndpointPair = New Windows.Networking.EndpointPair()

		Return result
	End Function

End Class