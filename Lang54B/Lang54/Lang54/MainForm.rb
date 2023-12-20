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
		@button1 = System::Windows::Forms::Button.new()
		@button2 = System::Windows::Forms::Button.new()
		@button3 = System::Windows::Forms::Button.new()
		@label1 = System::Windows::Forms::Label.new()
		@textBox1 = System::Windows::Forms::TextBox.new()
		@textBox2 = System::Windows::Forms::TextBox.new()
		@textBox3 = System::Windows::Forms::TextBox.new()
		self.SuspendLayout()
		# 
		# button1
		# 
		@button1.BackColor = System::Drawing::Color.Wheat
		@button1.Location = System::Drawing::Point.new(12, 373)
		@button1.Name = "button1"
		@button1.Size = System::Drawing::Size.new(142, 58)
		@button1.TabIndex = 0
		@button1.Text = "Calculate"
		@button1.UseVisualStyleBackColor = false
		@button1.Click { |sender, e| self.Button1Click(sender, e) }
		# 
		# button2
		# 
		@button2.BackColor = System::Drawing::Color.Wheat
		@button2.Location = System::Drawing::Point.new(160, 373)
		@button2.Name = "button2"
		@button2.Size = System::Drawing::Size.new(142, 58)
		@button2.TabIndex = 1
		@button2.Text = "Clear"
		@button2.UseVisualStyleBackColor = false
		@button2.Click { |sender, e| self.Button2Click(sender, e) }
		# 
		# button3
		# 
		@button3.BackColor = System::Drawing::Color.Wheat
		@button3.Location = System::Drawing::Point.new(308, 373)
		@button3.Name = "button3"
		@button3.Size = System::Drawing::Size.new(142, 58)
		@button3.TabIndex = 2
		@button3.Text = "Exit"
		@button3.UseVisualStyleBackColor = false
		@button3.Click { |sender, e| self.Button3Click(sender, e) }
		# 
		# label1
		# 
		@label1.BackColor = System::Drawing::Color.Tan
		@label1.Location = System::Drawing::Point.new(177, 151)
		@label1.Name = "label1"
		@label1.Size = System::Drawing::Size.new(273, 74)
		@label1.TabIndex = 3
		@label1.Click { |sender, e| self.Label1Click(sender, e) }
		# 
		# textBox1
		# 
		@textBox1.BackColor = System::Drawing::Color.NavajoWhite
		@textBox1.Location = System::Drawing::Point.new(12, 151)
		@textBox1.Name = "textBox1"
		@textBox1.Size = System::Drawing::Size.new(159, 20)
		@textBox1.TabIndex = 4
		@textBox1.TextChanged { |sender, e| self.TextBox1TextChanged(sender, e) }
		# 
		# textBox2
		# 
		@textBox2.BackColor = System::Drawing::Color.NavajoWhite
		@textBox2.Location = System::Drawing::Point.new(12, 205)
		@textBox2.Name = "textBox2"
		@textBox2.Size = System::Drawing::Size.new(159, 20)
		@textBox2.TabIndex = 5
		# 
		# textBox3
		# 
		@textBox3.BackColor = System::Drawing::Color.NavajoWhite
		@textBox3.Location = System::Drawing::Point.new(12, 179)
		@textBox3.Name = "textBox3"
		@textBox3.Size = System::Drawing::Size.new(159, 20)
		@textBox3.TabIndex = 6
		# 
		# MainForm
		# 
		self.ClientSize = System::Drawing::Size.new(963, 443)
		self.Controls.Add(@textBox3)
		self.Controls.Add(@textBox2)
		self.Controls.Add(@textBox1)
		self.Controls.Add(@label1)
		self.Controls.Add(@button3)
		self.Controls.Add(@button2)
		self.Controls.Add(@button1)
		self.Name = "MainForm"
		self.Text = "Lang54"
		self.ResumeLayout(false)
		self.PerformLayout()
	end

	def TextBox1TextChanged(sender, e)
		
	end

	def Label1Click(sender, e)
		
	end

	def Button1Click(sender, e)
		Sum = int(@textBox1.Text) + int(@textBox2.Text) + int(@textBox3.Text)
		@label1.Text = "Sum: " = str(Sum)
	end

	def Button2Click(sender, e)
		@textBox1.Text = ""
		@textBox2.Text = ""
		@textBox3.Text = ""
		@label1.Text = ""
	end

	def Button3Click(sender, e)
		Aplication.Exit()
	end
end

