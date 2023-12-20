require "mscorlib"
require "System.Windows.Forms, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089"
require "System.Drawing, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a"

class MainForm < System::Windows::Forms::Form
	def initialize()
		self.InitializeComponent()
	end

	def InitializeComponent()
		@button2 = System::Windows::Forms::Button.new()
		@label1 = System::Windows::Forms::Label.new()
		@button1 = System::Windows::Forms::Button.new()
		self.SuspendLayout()
		# 
		# button2
		# 
		@button2.BackColor = System::Drawing::SystemColors.Window
		@button2.Font = System::Drawing::Font.new("Microsoft Sans Serif", 21.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button2.Location = System::Drawing::Point.new(463, 285)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(160, 123)
		@button2.TabIndex = 5
		@button2.Text = "clear"
		@button2.UseVisualStyleBackColor = false
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# label1
		# 
		@label1.BackColor = System::Drawing::SystemColors.Info
		@label1.Font = System::Drawing::Font.new("Microsoft Sans Serif", 21.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label1.Location = System::Drawing::Point.new(209, 46)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(462, 217)
		@label1.TabIndex = 4
		@label1.TextAlign = System::Drawing::ContentAlignment.MiddleCenter
		# 
		# button1
		# 
		@button1.BackColor = System::Drawing::SystemColors.Window
		@button1.Font = System::Drawing::Font.new("Microsoft Sans Serif", 21.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@button1.Location = System::Drawing::Point.new(223, 285)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(160, 123)
		@button1.TabIndex = 3
		@button1.Text = "Show"
		@button1.UseVisualStyleBackColor = false
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# MainForm
		# 
		self.ClientSize = System::Drawing::Size.new(880, 454)
		self.Controls.Add(@button2)
		self.Controls.Add(@label1)
		self.Controls.Add(@button1)
		self.Name = "MainForm"
		self.Text = "PhoneNumbers"
		self.ResumeLayout(false)
	end

	def Button1Click(sender, e)
		@label1.Text = "Mcdonalds (608)752-0100 \n Wendys (608)752-1744 \n Burger Kings (608)754-5015 \n Culvers (608)756-2611 \n Hardees (608)757-1557"
	end

	def Button2Click(sender, e)
		@label1.Text = ""
	end
end

