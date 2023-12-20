import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._label1 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._textBox4 = System.Windows.Forms.TextBox()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Navy
		self._label1.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._label1.Location = System.Drawing.Point(12, 115)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(144, 52)
		self._label1.TabIndex = 0
		self._label1.Text = "Sum:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		self._label1.Click += self.Label1Click
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.CornflowerBlue
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(12, 12)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(100, 47)
		self._textBox1.TabIndex = 1
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.CornflowerBlue
		self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(118, 12)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(100, 47)
		self._textBox2.TabIndex = 3
		# 
		# textBox3
		# 
		self._textBox3.BackColor = System.Drawing.Color.CornflowerBlue
		self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox3.Location = System.Drawing.Point(12, 65)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(100, 47)
		self._textBox3.TabIndex = 4
		# 
		# textBox4
		# 
		self._textBox4.BackColor = System.Drawing.Color.CornflowerBlue
		self._textBox4.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox4.Location = System.Drawing.Point(118, 65)
		self._textBox4.Name = "textBox4"
		self._textBox4.Size = System.Drawing.Size(100, 47)
		self._textBox4.TabIndex = 5
		self._textBox4.TextChanged += self.TextBox4TextChanged
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Navy
		self._label2.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._label2.Location = System.Drawing.Point(162, 115)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(144, 52)
		self._label2.TabIndex = 6
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Navy
		self._label3.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._label3.Location = System.Drawing.Point(12, 180)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(144, 52)
		self._label3.TabIndex = 7
		self._label3.Text = "Sum:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		self._label3.Click += self.Label3Click
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Navy
		self._label4.ForeColor = System.Drawing.SystemColors.ButtonHighlight
		self._label4.Location = System.Drawing.Point(162, 180)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(144, 52)
		self._label4.TabIndex = 8
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.DodgerBlue
		self._button1.Location = System.Drawing.Point(13, 236)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(99, 39)
		self._button1.TabIndex = 9
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.DodgerBlue
		self._button2.Location = System.Drawing.Point(118, 236)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(99, 39)
		self._button2.TabIndex = 10
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.DodgerBlue
		self._button3.Location = System.Drawing.Point(223, 235)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(99, 39)
		self._button3.TabIndex = 11
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(336, 282)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox4)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Lang54b"
		self.Load += self.MainFormLoad
		self.ResumeLayout(False)
		self.PerformLayout()


	def Label1Click(self, sender, e):
		pass

	def TextBox4TextChanged(self, sender, e):
		pass

	def Label3Click(self, sender, e):
		pass

	def MainFormLoad(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		A = self._textBox1.Text
		B = self._textBox2.Text
		C = self._textBox3.Text
		D = self._textBox4.Text
		Sum = A + B + C + D
		Avg = float(Sum/4.0)
		
		self._label2.Text = str(Sum)
		self._label4.Text = float(Avg)