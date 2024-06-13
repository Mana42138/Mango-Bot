local Main = Instance.new("ScreenGui")
local MainFrame = Instance.new("Frame")
local ConnectDiscord = Instance.new("TextLabel")
local UIScale = Instance.new("UIScale")
local Users = Instance.new("Frame")
local UICorner = Instance.new("UICorner")
local UsersTitle = Instance.new("TextLabel")
local UIScale_2 = Instance.new("UIScale")
local Servers = Instance.new("Frame")
local UICorner_2 = Instance.new("UICorner")
local ServerTitle = Instance.new("TextLabel")
local ServerContainer = Instance.new("ScrollingFrame")
local UIListLayout = Instance.new("UIListLayout")
local UIScale_3 = Instance.new("UIScale")
local History = Instance.new("Frame")
local UICorner_3 = Instance.new("UICorner")
local Back = Instance.new("TextButton")
local UICorner_4 = Instance.new("UICorner")
local HistoryHolder = Instance.new("Frame")
local HistoryContainer = Instance.new("ScrollingFrame")
local UIListLayout_2 = Instance.new("UIListLayout")
local UIPadding = Instance.new("UIPadding")
local UICorner_5 = Instance.new("UICorner")
local HistoryTitle = Instance.new("TextLabel")
local UICorner_6 = Instance.new("UICorner")
local HistoryMgnify = Instance.new("Frame")
local UICorner_7 = Instance.new("UICorner")
local HistoryText = Instance.new("TextLabel")
local UIPadding_2 = Instance.new("UIPadding")
local UITextSizeConstraint = Instance.new("UITextSizeConstraint")
local Back_2 = Instance.new("TextButton")
local UICorner_8 = Instance.new("UICorner")

--Properties:

Main.Name = "Main"
Main.Parent = game.Players.LocalPlayer:WaitForChild("PlayerGui")
Main.ZIndexBehavior = Enum.ZIndexBehavior.Sibling
Main.IgnoreGuiInset = true
Main.ScreenInsets = Enum.ScreenInsets.None
Main.SafeAreaCompatibility = Enum.SafeAreaCompatibility.None
Main.ClipToDeviceSafeArea = false
Main.ResetOnSpawn = false

MainFrame.Name = "MainFrame"
MainFrame.Parent = Main
MainFrame.AnchorPoint = Vector2.new(0.5, 0.5)
MainFrame.BackgroundColor3 = Color3.fromRGB(6, 6, 6)
MainFrame.BorderColor3 = Color3.fromRGB(0, 0, 0)
MainFrame.BorderSizePixel = 0
MainFrame.Position = UDim2.new(0.5, 0, 0.5, 0)
MainFrame.Size = UDim2.new(1, 0, 1, 0)

ConnectDiscord.Name = "Connect Discord"
ConnectDiscord.Parent = MainFrame
ConnectDiscord.AnchorPoint = Vector2.new(0.5, 0.5)
ConnectDiscord.BackgroundColor3 = Color3.fromRGB(255, 255, 255)
ConnectDiscord.BackgroundTransparency = 1.000
ConnectDiscord.BorderColor3 = Color3.fromRGB(0, 0, 0)
ConnectDiscord.BorderSizePixel = 0
ConnectDiscord.Position = UDim2.new(0.5, 0, 0.147, 0)
ConnectDiscord.Size = UDim2.new(0.22158365, 0, 0.0891265571, 0)
ConnectDiscord.Font = Enum.Font.FredokaOne
ConnectDiscord.Text = "Connect Discord"
ConnectDiscord.TextColor3 = Color3.fromRGB(26, 106, 255)
ConnectDiscord.TextScaled = true
ConnectDiscord.TextSize = 14.000
ConnectDiscord.TextTransparency = 0.170
ConnectDiscord.TextWrapped = true

UIScale.Parent = ConnectDiscord

Users.Name = "Users"
Users.Parent = MainFrame
Users.AnchorPoint = Vector2.new(0.5, 0.5)
Users.BackgroundColor3 = Color3.fromRGB(9, 15, 25)
Users.BorderColor3 = Color3.fromRGB(0, 0, 0)
Users.BorderSizePixel = 0
Users.Position = UDim2.new(0.0919540226, 0, 0.554673731, 0)
Users.Size = UDim2.new(0.166028097, 0, 0.826481521, 0)

UICorner.CornerRadius = UDim.new(0.0399999991, 0)
UICorner.Parent = Users

UsersTitle.Name = "UsersTitle"
UsersTitle.Parent = Users
UsersTitle.BackgroundColor3 = Color3.fromRGB(255, 255, 255)
UsersTitle.BackgroundTransparency = 1.000
UsersTitle.BorderColor3 = Color3.fromRGB(0, 0, 0)
UsersTitle.BorderSizePixel = 0
UsersTitle.Position = UDim2.new(0, 0, 0.0103179682, 0)
UsersTitle.Size = UDim2.new(1, 0, 0.0662238598, 0)
UsersTitle.Font = Enum.Font.FredokaOne
UsersTitle.Text = "USERS"
UsersTitle.TextColor3 = Color3.fromRGB(26, 106, 255)
UsersTitle.TextScaled = true
UsersTitle.TextSize = 14.000
UsersTitle.TextWrapped = true

UIScale_2.Parent = Users

Servers.Name = "Servers"
Servers.Parent = MainFrame
Servers.AnchorPoint = Vector2.new(0.5, 0.5)
Servers.BackgroundColor3 = Color3.fromRGB(9, 15, 25)
Servers.BorderColor3 = Color3.fromRGB(0, 0, 0)
Servers.BorderSizePixel = 0
Servers.Position = UDim2.new(0.237228602, 0, 0.553379238, 0)
Servers.Size = UDim2.new(0.106562547, 0, 0.381734312, 0)

UICorner_2.CornerRadius = UDim.new(0.0399999991, 0)
UICorner_2.Parent = Servers

ServerTitle.Name = "ServerTitle"
ServerTitle.Parent = Servers
ServerTitle.BackgroundColor3 = Color3.fromRGB(255, 255, 255)
ServerTitle.BackgroundTransparency = 1.000
ServerTitle.BorderColor3 = Color3.fromRGB(0, 0, 0)
ServerTitle.BorderSizePixel = 0
ServerTitle.Position = UDim2.new(0, 0, 0.0103179151, 0)
ServerTitle.Size = UDim2.new(1, 0, 0.120193973, 0)
ServerTitle.Font = Enum.Font.FredokaOne
ServerTitle.Text = "SERVERS"
ServerTitle.TextColor3 = Color3.fromRGB(26, 106, 255)
ServerTitle.TextScaled = true
ServerTitle.TextSize = 14.000
ServerTitle.TextWrapped = true

ServerContainer.Name = "ServerContainer"
ServerContainer.Parent = Servers
ServerContainer.Active = true
ServerContainer.BackgroundColor3 = Color3.fromRGB(255, 255, 255)
ServerContainer.BackgroundTransparency = 1.000
ServerContainer.BorderColor3 = Color3.fromRGB(0, 0, 0)
ServerContainer.BorderSizePixel = 0
ServerContainer.Position = UDim2.new(0, 0, 0.184195668, 0)
ServerContainer.Size = UDim2.new(1, 0, 0.80032742, 0)
ServerContainer.ScrollBarThickness = 8

UIListLayout.Parent = ServerContainer
UIListLayout.HorizontalAlignment = Enum.HorizontalAlignment.Center
UIListLayout.SortOrder = Enum.SortOrder.LayoutOrder
UIListLayout.Padding = UDim.new(0.0500000007, 0)

UIScale_3.Parent = Servers

History.Name = "History"
History.Parent = MainFrame
History.AnchorPoint = Vector2.new(0.5, 0.5)
History.BackgroundColor3 = Color3.fromRGB(9, 15, 25)
History.BorderColor3 = Color3.fromRGB(0, 0, 0)
History.BorderSizePixel = 0
History.Position = UDim2.new(0.528146923, 0, 0.503798485, 0)
History.Size = UDim2.new(0.445660681, 0, 0.832993746, 0)
History.Visible = false

UICorner_3.CornerRadius = UDim.new(0.0299999993, 0)
UICorner_3.Parent = History

Back.Name = "Back"
Back.Parent = History
Back.AnchorPoint = Vector2.new(0.5, 0.5)
Back.BackgroundColor3 = Color3.fromRGB(14, 24, 40)
Back.BorderColor3 = Color3.fromRGB(0, 0, 0)
Back.BorderSizePixel = 0
Back.Position = UDim2.new(0.887719393, 0, 0.0703990534, 0)
Back.Size = UDim2.new(0.184157848, 0, 0.0729999915, 0)
Back.AutoButtonColor = false
Back.Font = Enum.Font.FredokaOne
Back.Text = "Back"
Back.TextColor3 = Color3.fromRGB(255, 255, 255)
Back.TextSize = 31.000
Back.TextWrapped = true

UICorner_4.CornerRadius = UDim.new(0.200000003, 0)
UICorner_4.Parent = Back

HistoryHolder.Name = "HistoryHolder"
HistoryHolder.Parent = History
HistoryHolder.BackgroundColor3 = Color3.fromRGB(14, 24, 40)
HistoryHolder.BorderColor3 = Color3.fromRGB(0, 0, 0)
HistoryHolder.BorderSizePixel = 0
HistoryHolder.Position = UDim2.new(0.0789473653, 0, 0.165146634, 0)
HistoryHolder.Size = UDim2.new(0.828070164, 0, 0.779153466, 0)

HistoryContainer.Name = "HistoryContainer"
HistoryContainer.Parent = HistoryHolder
HistoryContainer.Active = true
HistoryContainer.BackgroundColor3 = Color3.fromRGB(255, 255, 255)
HistoryContainer.BackgroundTransparency = 1.000
HistoryContainer.BorderColor3 = Color3.fromRGB(0, 0, 0)
HistoryContainer.BorderSizePixel = 0
HistoryContainer.Position = UDim2.new(0, 0, 0.0190217383, 0)
HistoryContainer.Size = UDim2.new(0.983050823, 0, 0.980978251, 0)
HistoryContainer.ScrollBarThickness = 8

UIListLayout_2.Parent = HistoryContainer
UIListLayout_2.HorizontalAlignment = Enum.HorizontalAlignment.Center
UIListLayout_2.SortOrder = Enum.SortOrder.LayoutOrder
UIListLayout_2.Padding = UDim.new(0.0299999993, 0)

UIPadding.Parent = HistoryContainer
UIPadding.PaddingLeft = UDim.new(0.0500000007, 0)
UIPadding.PaddingRight = UDim.new(0.0250000004, 0)
UIPadding.PaddingTop = UDim.new(0.00999999978, 0)

UICorner_5.CornerRadius = UDim.new(0.0299999993, 0)
UICorner_5.Parent = HistoryHolder

HistoryTitle.Name = "HistoryTitle"
HistoryTitle.Parent = History
HistoryTitle.BackgroundColor3 = Color3.fromRGB(14, 24, 40)
HistoryTitle.BorderColor3 = Color3.fromRGB(0, 0, 0)
HistoryTitle.BorderSizePixel = 0
HistoryTitle.Position = UDim2.new(0.219298244, 0, 0.0338762365, 0)
HistoryTitle.Size = UDim2.new(0.521052659, 0, 0.0730456412, 0)
HistoryTitle.Font = Enum.Font.FredokaOne
HistoryTitle.Text = "HISTORY"
HistoryTitle.TextColor3 = Color3.fromRGB(255, 255, 255)
HistoryTitle.TextScaled = true
HistoryTitle.TextSize = 14.000
HistoryTitle.TextWrapped = true

UICorner_6.CornerRadius = UDim.new(0.150000006, 0)
UICorner_6.Parent = HistoryTitle

HistoryMgnify.Name = "HistoryMgnify"
HistoryMgnify.Parent = History
HistoryMgnify.BackgroundColor3 = Color3.fromRGB(14, 24, 40)
HistoryMgnify.BorderColor3 = Color3.fromRGB(0, 0, 0)
HistoryMgnify.BorderSizePixel = 0
HistoryMgnify.Position = UDim2.new(0.0789473653, 0, 0.165146634, 0)
HistoryMgnify.Size = UDim2.new(0.828070164, 0, 0.779153466, 0)
HistoryMgnify.Visible = false

UICorner_7.CornerRadius = UDim.new(0.0299999993, 0)
UICorner_7.Parent = HistoryMgnify

HistoryText.Name = "HistoryText"
HistoryText.Parent = HistoryMgnify
HistoryText.BackgroundColor3 = Color3.fromRGB(255, 255, 255)
HistoryText.BackgroundTransparency = 1.000
HistoryText.BorderColor3 = Color3.fromRGB(0, 0, 0)
HistoryText.BorderSizePixel = 0
HistoryText.Size = UDim2.new(1, 0, 1, 0)
HistoryText.Font = Enum.Font.Arial
HistoryText.Text = "she said"
HistoryText.TextColor3 = Color3.fromRGB(255, 255, 255)
HistoryText.TextScaled = true
HistoryText.TextSize = 14.000
HistoryText.TextWrapped = true
HistoryText.TextXAlignment = Enum.TextXAlignment.Left
HistoryText.TextYAlignment = Enum.TextYAlignment.Top

UIPadding_2.Parent = HistoryText
UIPadding_2.PaddingLeft = UDim.new(0.0500000007, 0)
UIPadding_2.PaddingTop = UDim.new(0.0500000007, 0)

UITextSizeConstraint.Parent = HistoryText
UITextSizeConstraint.MaxTextSize = 15

Back_2.Name = "Back"
Back_2.Parent = HistoryMgnify
Back_2.BackgroundColor3 = Color3.fromRGB(23, 40, 65)
Back_2.BorderColor3 = Color3.fromRGB(0, 0, 0)
Back_2.BorderSizePixel = 0
Back_2.Position = UDim2.new(0.944915235, 0, -0.0315025449, 0)
Back_2.Size = UDim2.new(0.0614406765, 0, 0.0830521658, 0)
Back_2.AutoButtonColor = false
Back_2.Font = Enum.Font.FredokaOne
Back_2.Text = "X"
Back_2.TextColor3 = Color3.fromRGB(255, 255, 255)
Back_2.TextSize = 21.000
Back_2.TextWrapped = true

UICorner_8.Parent = Back_2



	local TweenService = game:GetService("TweenService")
	
	local History = game.Players.LocalPlayer.PlayerGui.Main.MainFrame.History
	
	ConnectDiscord.TextTransparency = 1
	Users.UIScale.Scale = 0.001
	Users.Visible = false
	Servers.Visible = false
	
	task.wait(1)
	
	TweenService:Create(
		ConnectDiscord,
		TweenInfo.new(.7, Enum.EasingStyle.Back),
		{TextTransparency = 0}
	):Play()
	
	task.wait(.5)
	
	Servers.Visible = true
	Users.Visible = true
	TweenService:Create(
		Users.UIScale,
		TweenInfo.new(.5, Enum.EasingStyle.Back),
		{Scale = 1}
	):Play()
	
	local Servers, users = {}, {}
	
	game.ReplicatedStorage.Transfer.OnClientEvent:Connect(function(typo, data)
		if typo == "Users" then
			for i,v in pairs(data) do
				local ServerID = string.match(i, "@(.+)")
				local ServerName = string.match(i, "^[^@]+")
				users[ServerName] = {}
				local NewContainer = game.ReplicatedStorage.UserContainer:Clone()
				NewContainer.Parent = Users
				NewContainer.Name = ServerName
				NewContainer.Visible = false
				
				local NewServer = game.ReplicatedStorage.ServerTemplate:Clone()
				NewServer.Parent = ServerContainer
				NewServer.Name = ServerName
				NewServer.Title.Text = ServerName
				
				NewServer.MouseButton1Click:Connect(function()
					for i,v in pairs(Users:GetChildren()) do
						if v:IsA("ScrollingFrame") then
							v.Visible = false
						end
					end
					NewContainer.Visible = true
				end)
				
				for i1,v1 in pairs(v) do
					users[ServerName][v1.ID] = {
						["DisplayName"] = v1.DisplayName,
						["Name"] = "@"..v1.Name,
						["ID"] = v1.ID
					}
					local User = game.ReplicatedStorage.Template:Clone()
					User.Parent = Users[ServerName]
					User.Title.Text = v1.DisplayName
					User.Username.Text = "@"..v1.Name
					User.ID.Value = v1.ID
					User.SID.Value = ServerID
				end
			end
			
		elseif typo == "msg" then
			local data = data.data
			for i,v in pairs(data) do
				local UserID = string.match(i, "^[^@]+")
				if UserID == tostring(game.Players.LocalPlayer.UserId) then
					for i,v in pairs(v) do
						if v == "" then v = "Unknown" end
						local NewText = game.ReplicatedStorage.TextChat:Clone()
						NewText.Parent = HistoryContainer
						NewText.Text = tostring(v)
						NewText.Visible = true
						task.wait(0.001)
					end
				end
			end
			print(data)
		end
		
	end)

	
	Back_2.MouseButton1Click:Connect(function()
		HistoryMgnify.Visible = false
		HistoryHolder.Visible = true
	end)
	
	Back.MouseButton1Click:Connect(function()
		History.Visible = false
	end)

