import math
import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label1 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label9 = System.Windows.Forms.Label()
		self._label10 = System.Windows.Forms.Label()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._label11 = System.Windows.Forms.Label()
		self._label12 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(13, 358)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(82, 33)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(101, 358)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(82, 33)
		self._button2.TabIndex = 1
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(189, 358)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(82, 33)
		self._button3.TabIndex = 2
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Crimson
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 61)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(159, 49)
		self._label1.TabIndex = 3
		self._label1.Text = "Change:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		self._label1.Click += self.Label1Click
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(27, 11)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(144, 47)
		self._textBox1.TabIndex = 4
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Crimson
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(12, 110)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(159, 49)
		self._label2.TabIndex = 5
		self._label2.Text = "Dollars:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Crimson
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(12, 159)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(159, 49)
		self._label3.TabIndex = 6
		self._label3.Text = "Quarters:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Crimson
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(12, 208)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(159, 49)
		self._label4.TabIndex = 7
		self._label4.Text = "Dimes:"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.Crimson
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(12, 257)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(159, 49)
		self._label5.TabIndex = 8
		self._label5.Text = "Nickles:"
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.Crimson
		self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(12, 306)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(159, 49)
		self._label6.TabIndex = 13
		self._label6.Text = "Pennies:"
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.Crimson
		self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.Location = System.Drawing.Point(189, 61)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(159, 49)
		self._label7.TabIndex = 12
		self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.Crimson
		self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.Location = System.Drawing.Point(189, 110)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(159, 49)
		self._label8.TabIndex = 11
		self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.Color.Crimson
		self._label9.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label9.Location = System.Drawing.Point(189, 159)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(159, 49)
		self._label9.TabIndex = 10
		self._label9.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.Color.Crimson
		self._label10.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label10.Location = System.Drawing.Point(189, 208)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(159, 49)
		self._label10.TabIndex = 9
		self._label10.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		self._label10.Click += self.Label10Click
		# 
		# textBox2
		# 
		self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(189, 11)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(144, 47)
		self._textBox2.TabIndex = 15
		# 
		# label11
		# 
		self._label11.BackColor = System.Drawing.Color.Crimson
		self._label11.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label11.Location = System.Drawing.Point(189, 257)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(159, 49)
		self._label11.TabIndex = 16
		self._label11.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label12
		# 
		self._label12.BackColor = System.Drawing.Color.Crimson
		self._label12.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label12.Location = System.Drawing.Point(189, 306)
		self._label12.Name = "label12"
		self._label12.Size = System.Drawing.Size(159, 49)
		self._label12.TabIndex = 17
		self._label12.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(369, 425)
		self.Controls.Add(self._label12)
		self.Controls.Add(self._label11)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._label10)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "Lang58t"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Label1Click(self, sender, e):
		pass

	def Label10Click(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		Cost = float(self._textBox1.Text)
		Pay = float(self._textBox2.Text)
		Change = Pay - Cost
		self._label7.Text = str(Change)
		Dollars = Change//1
		self._label8.Text = str(Dollars)
		Quarters = (Change - Dollars)//.25
		self._label9.Text = str(Quarters)
		Dimes = (Change - Dollars - (Quarters * .25)) * 10 //1
		self._label10.Text = str(Dimes)
		Nickles = (Change - Dollars - (Quarters * .25) - (Dimes * .10)) * 20 //1
		self._label11.Text = str(Nickles)
		Pennies = (Change - Dollars - (Quarters * .25) - (Dimes * .10) - (Nickles * .05)) * 100
		self._label12.Text = str(Pennies)

	def Button2Click(self, sender, e):
		self._label7.Text = ""
		self._label8.Text = ""
		self._label9.Text = ""
		self._label10.Text = ""
		self._label11.Text = ""
		self._label12.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()