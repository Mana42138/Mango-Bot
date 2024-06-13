return function()

	local TextChat = Instance.new("TextButton")
	local UITextSizeConstraint = Instance.new("UITextSizeConstraint")
	local UIPadding = Instance.new("UIPadding")
	local UICorner = Instance.new("UICorner")
	local UIScale = Instance.new("UIScale")

	TextChat.Name = "TextChat"
	TextChat.Parent = game.ReplicatedStorage
	TextChat.AnchorPoint = Vector2.new(0.5, 0.5)
	TextChat.BackgroundColor3 = Color3.fromRGB(255, 255, 255)
	TextChat.BackgroundTransparency = 1.000
	TextChat.BorderColor3 = Color3.fromRGB(0, 0, 0)
	TextChat.BorderSizePixel = 0
	TextChat.Position = UDim2.new(0.467000008, 0, 0.0719999969, 0)
	TextChat.Size = UDim2.new(0.934000015, 0, 0.123000003, 0)
	TextChat.AutoButtonColor = false
	TextChat.Font = Enum.Font.Arial
	TextChat.TextColor3 = Color3.fromRGB(255, 255, 255)
	TextChat.TextScaled = true
	TextChat.TextSize = 14.000
	TextChat.TextWrapped = true
	TextChat.TextXAlignment = Enum.TextXAlignment.Left

	UITextSizeConstraint.Parent = TextChat
	UITextSizeConstraint.MaxTextSize = 15

	UIPadding.Parent = TextChat
	UIPadding.PaddingLeft = UDim.new(0.0399999991, 0)

	UICorner.CornerRadius = UDim.new(0.100000001, 0)
	UICorner.Parent = TextChat

	UIScale.Parent = TextChat


	local Button = TextChat
	local TweenService = game:GetService("TweenService")
	local History = game.Players.LocalPlayer.PlayerGui.Main.MainFrame.History

	Button.MouseEnter:Connect(function()
		TweenService:Create(
			Button.UIScale,
			TweenInfo.new(0.2, Enum.EasingStyle.Back),
			{Scale = 1.1}
		):Play()
	end)

	Button.MouseLeave:Connect(function()
		TweenService:Create(
			Button.UIScale,
			TweenInfo.new(0.2, Enum.EasingStyle.Back),
			{Scale = 1}
		):Play()
	end)

	Button.MouseButton1Down:Connect(function()
		TweenService:Create(
			Button.UIScale,
			TweenInfo.new(0.2, Enum.EasingStyle.Back),
			{Scale = 0.9}
		):Play()
	end)

	Button.MouseButton1Up:Connect(function()
		TweenService:Create(
			Button.UIScale,
			TweenInfo.new(0.2, Enum.EasingStyle.Back),
			{Scale = 1}
		):Play()
	end)

	Button.MouseButton1Click:Connect(function()
		History.HistoryMgnify.Visible = true
		History.HistoryMgnify.HistoryText.Text = Button.Text
		History.HistoryHolder.Visible = true
	end)

	return Button
end