import math
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
		self._label2 = System.Windows.Forms.Label()
		self._label3 = System.Windows.Forms.Label()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label9 = System.Windows.Forms.Label()
		self._label10 = System.Windows.Forms.Label()
		self._label11 = System.Windows.Forms.Label()
		self._label12 = System.Windows.Forms.Label()
		self._button1 = System.Windows.Forms.Button()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.Turquoise
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(12, 15)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(227, 40)
		self._label1.TabIndex = 0
		self._label1.Text = "KiloWatts Used:"
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.Teal
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(245, 16)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(135, 40)
		self._textBox1.TabIndex = 1
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.Cyan
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(12, 59)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(158, 51)
		self._label2.TabIndex = 2
		self._label2.Text = "Base Rate:"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		self._label2.Click += self.Label2Click
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.Cyan
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(12, 110)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(158, 51)
		self._label3.TabIndex = 3
		self._label3.Text = "Surcharge:"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.Cyan
		self._label4.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label4.Location = System.Drawing.Point(12, 161)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(158, 51)
		self._label4.TabIndex = 4
		self._label4.Text = "City Tax:"
		self._label4.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.Cyan
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 18, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(176, 59)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(139, 51)
		self._label5.TabIndex = 5
		self._label5.Text = "$0.0475 per hour"
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.Cyan
		self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(321, 59)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(158, 51)
		self._label6.TabIndex = 6
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.Cyan
		self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.Location = System.Drawing.Point(321, 110)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(158, 51)
		self._label7.TabIndex = 7
		self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label8
		# 
		self._label8.BackColor = System.Drawing.Color.Cyan
		self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.Location = System.Drawing.Point(321, 161)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(158, 51)
		self._label8.TabIndex = 8
		self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.Color.Cyan
		self._label9.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label9.Location = System.Drawing.Point(12, 212)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(158, 51)
		self._label9.TabIndex = 9
		self._label9.Text = "Pay:"
		self._label9.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.Color.Cyan
		self._label10.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label10.Location = System.Drawing.Point(321, 212)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(158, 51)
		self._label10.TabIndex = 10
		self._label10.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label11
		# 
		self._label11.BackColor = System.Drawing.Color.Cyan
		self._label11.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label11.Location = System.Drawing.Point(12, 263)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(227, 51)
		self._label11.TabIndex = 11
		self._label11.Text = "Pay 5 days late:"
		self._label11.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# label12
		# 
		self._label12.BackColor = System.Drawing.Color.Cyan
		self._label12.Font = System.Drawing.Font("Microsoft Sans Serif", 21.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label12.Location = System.Drawing.Point(321, 263)
		self._label12.Name = "label12"
		self._label12.Size = System.Drawing.Size(158, 51)
		self._label12.TabIndex = 12
		self._label12.TextAlign = System.Drawing.ContentAlignment.MiddleLeft
		# 
		# button1
		# 
		self._button1.Location = System.Drawing.Point(13, 318)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(145, 66)
		self._button1.TabIndex = 13
		self._button1.Text = "button1"
		self._button1.UseVisualStyleBackColor = True
		self._button1.Click += self.Button1Click
		# 
		# MainForm
		# 
		self.ClientSize = System.Drawing.Size(753, 483)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._label12)
		self.Controls.Add(self._label11)
		self.Controls.Add(self._label10)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "Lang93A"
		self.Load += self.MainFormLoad
		self.ResumeLayout(False)
		self.PerformLayout()


	def MainFormLoad(self, sender, e):
		pass

	def Label2Click(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		KWU = int(self._textBox1.Text)
		BasRat = KWU * 0.0475
		SurChrg = BasRat / 10
		CtyTax = BasRat * .03
		BasRat = round(BasRat, 2)
		SurChrg = round(SurChrg, 2)
		CtyTax = round(CtyTax, 2)
		PTA = float(BasRat) + float(SurChrg) + float(CtyTax)
		ATPL = PTA * 1.04
		PTA = round(PTA, 2)
		ATPL = round(ATPL, 2)
		
		self._label6.Text = str(BasRat)
		self._label7.Text = str(SurChrg)
		self._label8.Text = str(CtyTax)
		self._label10.Text = str(PTA)
		self._label12.Text = str(ATPL)