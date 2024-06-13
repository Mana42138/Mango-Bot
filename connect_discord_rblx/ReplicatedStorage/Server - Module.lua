return function()

	local ServerTemplate = Instance.new("TextButton")
	local UICorner = Instance.new("UICorner")
	local Title = Instance.new("TextLabel")
	local UITextSizeConstraint = Instance.new("UITextSizeConstraint")
	local UIScale = Instance.new("UIScale")

	ServerTemplate.Name = "ServerTemplate"
	ServerTemplate.Parent = game.ReplicatedStorage
	ServerTemplate.AnchorPoint = Vector2.new(0.5, 0.5)
	ServerTemplate.BackgroundColor3 = Color3.fromRGB(25, 54, 86)
	ServerTemplate.BorderColor3 = Color3.fromRGB(0, 0, 0)
	ServerTemplate.BorderSizePixel = 0
	ServerTemplate.Position = UDim2.new(0.5, 0, 0.0732646137, 0)
	ServerTemplate.Size = UDim2.new(0.769230723, 0, 0.146529227, 0)
	ServerTemplate.AutoButtonColor = false
	ServerTemplate.Font = Enum.Font.SourceSans
	ServerTemplate.Text = ""
	ServerTemplate.TextColor3 = Color3.fromRGB(0, 0, 0)
	ServerTemplate.TextSize = 14.000

	UICorner.CornerRadius = UDim.new(0.150000006, 0)
	UICorner.Parent = ServerTemplate

	Title.Name = "Title"
	Title.Parent = ServerTemplate
	Title.AnchorPoint = Vector2.new(0.5, 0.5)
	Title.BackgroundColor3 = Color3.fromRGB(255, 255, 255)
	Title.BackgroundTransparency = 1.000
	Title.BorderColor3 = Color3.fromRGB(0, 0, 0)
	Title.BorderSizePixel = 0
	Title.Position = UDim2.new(0.5, 0, 0.49999997, 0)
	Title.Size = UDim2.new(1, 0, 0.99999994, 0)
	Title.Font = Enum.Font.FredokaOne
	Title.Text = "Raiders Inc."
	Title.TextColor3 = Color3.fromRGB(255, 255, 255)
	Title.TextScaled = true
	Title.TextSize = 14.000
	Title.TextWrapped = true

	UITextSizeConstraint.Parent = Title
	UITextSizeConstraint.MaxTextSize = 20
	UITextSizeConstraint.MinTextSize = 10

	UIScale.Parent = ServerTemplate


	local Button = ServerTemplate
	local TweenService = game:GetService("TweenService")

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

	end)

	return ServerTemplate
end