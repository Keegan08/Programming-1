def int(text)     return text.to_i end
def float(text)   return text.to_f end
def str(text)     return text.to_s end
def list(obj)     return obj.to_a  end
def len(arr)      return arr.length end
def input(msg="") print msg; return gets end
def print(*args)  Kernel.print(*args, "\n") end
def round(x, y)   return float((x * 10**y).round) / 10**y end
def range(*args)  if len(args) == 1 then 
    return  list((0...args[0]).step(1)); elsif len(args) == 2 then 
    return  list((args[0]...args[1]).step(1)); elsif len(args) == 3 then 
    return  list((args[0]...args[1]).step(args[2])) end; end
class MyRandom;   def randint(min, max) return rand(max-min) + min; end; 
    def random() return rand() end; 
    def shuffle(arr) return arr.shuffle end; 
    def choice(arr) return arr[randint(0, len(arr))] end; 
end; $random = MyRandom.new(); $math = Math
MessageBox = System::Windows::Forms::MessageBox
require "mscorlib"
require "System.Windows.Forms, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089"
require "System.Drawing, Version=2.0.0.0, Culture=neutral, PublicKeyToken=b03f5f7f11d50a3a"

class MainForm < System::Windows::Forms::Form
	def initialize()
		self.InitializeComponent()
	end

	def InitializeComponent()
		@textBox1 = System::Windows::Forms::TextBox.new()
		@textBox2 = System::Windows::Forms::TextBox.new()
		@textBox3 = System::Windows::Forms::TextBox.new()
		@textBox4 = System::Windows::Forms::TextBox.new()
		@label1 = System::Windows::Forms::Label.new()
		@label2 = System::Windows::Forms::Label.new()
		@button1 = System::Windows::Forms::Button.new()
		@button2 = System::Windows::Forms::Button.new()
		@button3 = System::Windows::Forms::Button.new()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		@textBox1.Location = System::Drawing::Point.new(145, 107)
		@textBox1.Name = "textBox1"
		@textBox1.Size = System::Drawing::Size.new(190, 20)
		@textBox1.TabIndex = 0
		# 
		# textBox2
		# 
		@textBox2.Location = System::Drawing::Point.new(145, 133)
		@textBox2.Name = "textBox2"
		@textBox2.Size = System::Drawing::Size.new(190, 20)
		@textBox2.TabIndex = 1
		# 
		# textBox3
		# 
		@textBox3.Location = System::Drawing::Point.new(145, 159)
		@textBox3.Name = "textBox3"
		@textBox3.Size = System::Drawing::Size.new(190, 20)
		@textBox3.TabIndex = 2
		# 
		# textBox4
		# 
		@textBox4.Location = System::Drawing::Point.new(145, 185)
		@textBox4.Name = "textBox4"
		@textBox4.Size = System::Drawing::Size.new(190, 20)
		@textBox4.TabIndex = 3
		# 
		# label1
		# 
		@label1.BackColor = System::Drawing::Color.Moccasin
		@label1.Font = System::Drawing::Font.new("Microsoft Sans Serif", 21.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label1.Location = System::Drawing::Point.new(360, 107)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(208, 46)
		@label1.TabIndex = 4
		@label1.Text = "Average:"
		@label1.TextAlign = System::Drawing::ContentAlignment.MiddleLeft
		# 
		# label2
		# 
		@label2.BackColor = System::Drawing::Color.Moccasin
		@label2.Font = System::Drawing::Font.new("Microsoft Sans Serif", 21.75, System::Drawing::FontStyle.Regular, System::Drawing::GraphicsUnit.Point, 0)
		@label2.Location = System::Drawing::Point.new(360, 159)
		@label2.Name = "label2"
		@label2.Size = System::Drawing::Size.new(208, 46)
		@label2.TabIndex = 5
		@label2.Text = "Sum:"
		@label2.TextAlign = System::Drawing::ContentAlignment.MiddleLeft
		# 
		# button1
		# 
		@button1.Location = System::Drawing::Point.new(145, 212)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(127, 49)
		@button1.TabIndex = 6
		@button1.Text = "Calculate"
		@button1.UseVisualStyleBackColor = true
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# button2
		# 
		@button2.Location = System::Drawing::Point.new(278, 211)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(127, 49)
		@button2.TabIndex = 7
		@button2.Text = "Clear"
		@button2.UseVisualStyleBackColor = true
		# 
		# button3
		# 
		@button3.Location = System::Drawing::Point.new(411, 212)
		@button3.Name = "button3"
		@button3.Size = System::Drawing::Size.new(127, 49)
		@button3.TabIndex = 8
		@button3.Text = "Exit"
		@button3.UseVisualStyleBackColor = true
		# 
		# MainForm
		# 
		self.ClientSize = System::Drawing::Size.new(854, 430)
		self.Controls.Add(@button3)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Controls.Add(@label2)
		self.Controls.Add(@label1)
		self.Controls.Add(@textBox4)
		self.Controls.Add(@textBox3)
		self.Controls.Add(@textBox2)
		self.Controls.Add(@textBox1)
		self.Name = "MainForm"
		self.Text = "Lang54B"
		self.ResumeLayout(false)
		self.PerformLayout()
	end

	def Button1Click(sender, e)
		A = int(@textBox1.Text)
		B = int(@textBox2.Text)
		C = int(@textBox3.Text)
		D = int(@textBox4.Text
		Sum = A + B + C + D
		Average = (Sum/4.0)
		@label2.Text = "Average: " + str(Average)
		@label1.Text = "Sum:: " + str(Sum)
	end
end

@textBox1.Text = ""
		@textBox2.Text = ""
		@textBox3.Text = ""
		@label1.Text = "Sum:"
		@label2.Text = "Average:"