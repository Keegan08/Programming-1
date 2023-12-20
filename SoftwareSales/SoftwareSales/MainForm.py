import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label3 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.DarkBlue
		self._label1.Location = System.Drawing.Point(175, 50)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(250, 250)
		self._label1.TabIndex = 0
		# 
		# label2
		# 
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.ForeColor = System.Drawing.SystemColors.ControlLight
		self._label2.Location = System.Drawing.Point(175, 50)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(100, 25)
		self._label2.TabIndex = 1
		self._label2.Text = "Quantity sold"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# textBox1
		# 
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(325, 100)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 31)
		self._textBox1.TabIndex = 2
		# 
		# label3
		# 
		self._label3.Location = System.Drawing.Point(175, 100)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(100, 31)
		self._label3.TabIndex = 3
		self._label3.Text = "label3"
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Navy
		self.ClientSize = System.Drawing.Size(584, 561)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "SoftwareSales"
		self.ResumeLayout(False)
		self.PerformLayout()

