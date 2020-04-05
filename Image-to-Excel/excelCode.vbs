Sub colorMeElmo()
	Dim r As Object
	For Each r In Selection
		ary = Split(r.Value, " ")
		r.Interior.Color = RGB(ary(0), ary(1), ary(2))
	Next r
End Sub
