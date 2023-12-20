import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button1 = System.Windows.Forms.Button()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Lime
		self._button1.Location = System.Drawing.Point(29, 185)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(108, 48)
		self._button1.TabIndex = 0
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.MediumSpringGreen
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(13, 13)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(124, 40)
		self._textBox1.TabIndex = 1
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.MediumSpringGreen
		self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(143, 13)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(124, 40)
		self._textBox2.TabIndex = 2
		# 
		# textBox3
		# 
		self._textBox3.BackColor = System.Drawing.Color.MediumSpringGreen
		self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox3.Location = System.Drawing.Point(79, 59)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(124, 40)
		self._textBox3.TabIndex = 3
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.LawnGreen
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(35, 102)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(218, 80)
		self._label1.TabIndex = 4
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Lime
		self._button2.Location = System.Drawing.Point(143, 185)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(108, 48)
		self._button2.TabIndex = 5
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Lime
		self._button3.Location = System.Drawing.Point(86, 239)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(108, 48)
		self._button3.TabIndex = 6
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(348, 393)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._button1)
		self.Name = "MainForm"
		self.Text = "MSOEpractice1"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		Day = float(self._textBox1.Text)
		Month = float(self._textBox2.Text)
		Year = float(self._textBox3.Text)
		A = (14 - Month)/12
		Y = Year + 4800 - A
		M = Month + (12*A) - 3
		JD = Day + (((153*M) + 2)/5) + (365*Y) + (Y/4) - (Y/100) + (Y/400) - 32045
		self._label1.Text = str(JD)

	def Button2Click(self, sender, e):
		self._label1.Text = ""

	def Button3Click(self, sender, e):
		application.Exit()