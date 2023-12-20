import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._listBox1 = System.Windows.Forms.ListBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# listBox1
		# 
		self._listBox1.BackColor = System.Drawing.Color.DarkRed
		self._listBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 12, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._listBox1.FormattingEnabled = True
		self._listBox1.ItemHeight = 20
		self._listBox1.Location = System.Drawing.Point(12, 12)
		self._listBox1.Name = "listBox1"
		self._listBox1.Size = System.Drawing.Size(796, 364)
		self._listBox1.TabIndex = 0
		self._listBox1.SelectedIndexChanged += self.ListBox1SelectedIndexChanged
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.Brown
		self._button1.Location = System.Drawing.Point(13, 400)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(125, 54)
		self._button1.TabIndex = 1
		self._button1.Text = "button1"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.Brown
		self._button2.Location = System.Drawing.Point(144, 399)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(125, 54)
		self._button2.TabIndex = 2
		self._button2.Text = "button2"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.Brown
		self._button3.Location = System.Drawing.Point(275, 399)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(125, 54)
		self._button3.TabIndex = 3
		self._button3.Text = "button3"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Firebrick
		self.ClientSize = System.Drawing.Size(839, 613)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._listBox1)
		self.Name = "MainForm"
		self.Text = "prog122c"
		self.ResumeLayout(False)


	def Button1Click(self, sender, e):
		for num in range(1, 40+1):
			Col1 = num * 2
			Col2 = Col1 + 1
			Col3 = Col1 * 2
			Col4 = Col1 * Col1
			msg = str(Col1) + "\t\t" + str(Col2) + "\t\t" + str(Col3) + "\t\t" + str(Col4)
			self._listBox1.Items.Add(msg)

	def Button2Click(self, sender, e):
		self._listBox1.Items.Clear()

	def Button3Click(self, sender, e):
		Application.Exit()

	def ListBox1SelectedIndexChanged(self, sender, e):
		pass