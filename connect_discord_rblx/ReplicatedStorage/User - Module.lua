return function(MainFrame)

	local Template = Instance.new("TextButton")
	local UICorner = Instance.new("UICorner")
	local Title = Instance.new("TextLabel")
	local UITextSizeConstraint = Instance.new("UITextSizeConstraint")
	local Username = Instance.new("TextLabel")
	local UITextSizeConstraint_2 = Instance.new("UITextSizeConstraint")
	local UIScale = Instance.new("UIScale")
	local SID = Instance.new("StringValue")
	local ID = Instance.new("StringValue")
	
	Template.Name = "Template"
	Template.Parent = game.ReplicatedStorage
	Template.AnchorPoint = Vector2.new(0.5, 0.5)
	Template.BackgroundColor3 = Color3.fromRGB(25, 54, 86)
	Template.BorderColor3 = Color3.fromRGB(0, 0, 0)
	Template.BorderSizePixel = 0
	Template.Position = UDim2.new(0.5, 0, 0.0499217324, 0)
	Template.Size = UDim2.new(0.769230783, 0, 0.0998435318, 0)
	Template.AutoButtonColor = false
	Template.Font = Enum.Font.SourceSans
	Template.Text = ""
	Template.TextColor3 = Color3.fromRGB(0, 0, 0)
	Template.TextSize = 14.000

	UICorner.CornerRadius = UDim.new(0.150000006, 0)
	UICorner.Parent = Template

	Title.Name = "Title"
	Title.Parent = Template
	Title.AnchorPoint = Vector2.new(0.5, 0.5)
	Title.BackgroundColor3 = Color3.fromRGB(255, 255, 255)
	Title.BackgroundTransparency = 1.000
	Title.BorderColor3 = Color3.fromRGB(0, 0, 0)
	Title.BorderSizePixel = 0
	Title.Position = UDim2.new(0.417499989, 0, 0.270312339, 0)
	Title.Size = UDim2.new(0.764999986, 0, 0.540624678, 0)
	Title.Font = Enum.Font.FredokaOne
	Title.Text = "Mana"
	Title.TextColor3 = Color3.fromRGB(255, 255, 255)
	Title.TextScaled = true
	Title.TextSize = 14.000
	Title.TextWrapped = true
	Title.TextXAlignment = Enum.TextXAlignment.Left
	
	ID.Parent = Template
	ID.Name = "ID"
	ID.Value = ""
	
	SID.Parent = Template
	SID.Name = "SID"
	SID.Value = ""

	UITextSizeConstraint.Parent = Title
	UITextSizeConstraint.MaxTextSize = 20
	UITextSizeConstraint.MinTextSize = 10

	Username.Name = "Username"
	Username.Parent = Template
	Username.AnchorPoint = Vector2.new(0.5, 0.5)
	Username.BackgroundColor3 = Color3.fromRGB(255, 255, 255)
	Username.BackgroundTransparency = 1.000
	Username.BorderColor3 = Color3.fromRGB(0, 0, 0)
	Username.BorderSizePixel = 0
	Username.Position = UDim2.new(0.417499989, 0, 0.703320146, 0)
	Username.Size = UDim2.new(0.764999986, 0, 0.325390905, 0)
	Username.Font = Enum.Font.FredokaOne
	Username.Text = "@mana_dw"
	Username.TextColor3 = Color3.fromRGB(153, 153, 153)
	Username.TextScaled = true
	Username.TextSize = 14.000
	Username.TextWrapped = true
	Username.TextXAlignment = Enum.TextXAlignment.Left

	UITextSizeConstraint_2.Parent = Username
	UITextSizeConstraint_2.MaxTextSize = 20
	UITextSizeConstraint_2.MinTextSize = 10

	UIScale.Parent = Template


	local Button = Template
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
			for i,v in pairs(MainFrame.History.HistoryHolder.HistoryContainer:GetChildren()) do
				if v:IsA("TextButton") then
					v:Destroy()
				end
			end
			MainFrame.History.Visible = true
			game.ReplicatedStorage.Transfer:FireServer(tostring(ID.Value), tostring(SID.Value))
		end)
		
	return Template
end