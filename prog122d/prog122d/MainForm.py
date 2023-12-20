import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._button3 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button1 = System.Windows.Forms.Button()
		self._listBox1 = System.Windows.Forms.ListBox()
		self.SuspendLayout()
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(294, 360)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(113, 53)
		self._button3.TabIndex = 7
		self._button3.Text = "button3"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(150, 360)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(113, 53)
		self._button2.TabIndex = 6
		self._button2.Text = "button2"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(12, 360)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(113, 53)
		self._button1.TabIndex = 5
		self._button1.Text = "button1"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# listBox1
		# 
		self._listBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._listBox1.FormattingEnabled = True
		self._listBox1.ItemHeight = 33
		self._listBox1.Location = System.Drawing.Point(12, 12)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(666, 334)
		self._listBox1.TabIndex = 4
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(874, 559)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._listBox1)
		self.Name = "MainForm"
		self.Text = "prog122d"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		for num in range(-12, 16+1):
			othernum = (num**6) - ((num**5)*3) - ((num**4)*93) + ((num**3)*87) + ((num**2)*1596) - (num*1380) - 2800
			msg = str(num) + "\t\t" + str(othernum)
			self._listBox1.Items.Add(msg)

	def Button2Click(self, sender, e):
		self._listBox1.Items.Clear()

	def Button3Click(self, sender, e):
		Application.Exit()