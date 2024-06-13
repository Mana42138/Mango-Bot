return function()

	local UserContainer = Instance.new("ScrollingFrame")
	local UIListLayout = Instance.new("UIListLayout")

	UserContainer.Name = "UserContainer"
	UserContainer.Parent = game.ReplicatedStorage
	UserContainer.Active = true
	UserContainer.BackgroundColor3 = Color3.fromRGB(255, 255, 255)
	UserContainer.BackgroundTransparency = 1.000
	UserContainer.BorderColor3 = Color3.fromRGB(0, 0, 0)
	UserContainer.BorderSizePixel = 0
	UserContainer.Position = UDim2.new(0, 0, 0.092861712, 0)
	UserContainer.Size = UDim2.new(1, 0, 0.891661346, 0)
	UserContainer.Visible = false
	UserContainer.ScrollBarThickness = 8

	UIListLayout.Parent = UserContainer
	UIListLayout.HorizontalAlignment = Enum.HorizontalAlignment.Center
	UIListLayout.SortOrder = Enum.SortOrder.LayoutOrder
	UIListLayout.Padding = UDim.new(0.00999999978, 0)
	
	return UserContainer
end