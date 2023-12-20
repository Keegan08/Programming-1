import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
	
	def InitializeComponent(self):
		self._textBox1 = System.Windows.Forms.TextBox()
		self._label1 = System.Windows.Forms.Label()
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label4 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.BurlyWood
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(224, 12)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(145, 40)
		self._textBox1.TabIndex = 0
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.DarkGoldenrod
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 9)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(206, 49)
		self._label1.TabIndex = 1
		self._label1.Text = "Speed Limit:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.DarkGoldenrod
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(12, 58)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(206, 49)
		self._label2.TabIndex = 2
		self._label2.Text = "Speed:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.DarkGoldenrod
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(12, 107)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(206, 49)
		self._label3.TabIndex = 3
		self._label3.Text = "Ticket Price:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.BurlyWood
		self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(224, 58)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(145, 40)
		self._textBox2.TabIndex = 4
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(13, 160)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(107, 60)
		self._button1.TabIndex = 6
		self._button1.Text = "Calculate"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.Location = System.Drawing.Point(126, 159)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(107, 60)
		self._button2.TabIndex = 7
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = True
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.Location = System.Drawing.Point(239, 159)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(107, 60)
		self._button3.TabIndex = 8
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = True
		self._button3.Click += self.Button3Click
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.DarkGoldenrod
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(214, 107)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(206, 49)
		self._label4.TabIndex = 9
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		self._label4.Click += self.Label4Click
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Goldenrod
		self.ClientSize = System.Drawing.Size(496, 273)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Controls.Add(self._textBox1)
		self.Name = "MainForm"
		self.Text = "Lang82A"
		self.ResumeLayout(False)
		self.PerformLayout()


	def Button1Click(self, sender, e):
		SpdLmt = int(self._textBox1.Text)
		Spd = int(self._textBox2.Text)
		SpdDif = int(Spd) - int(SpdLmt)
		TktPrc = (int(SpdDif) * 5) + 20

		self._label4.Text = str(TktPrc)
	def Label4Click(self, sender, e):
		pass

	def Button2Click(self, sender, e):
		self._label4.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()