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
		self._label3 = System.Windows.Forms.Label()
		self._textBox1 = System.Windows.Forms.TextBox()
		self._textBox2 = System.Windows.Forms.TextBox()
		self._textBox3 = System.Windows.Forms.TextBox()
		self._textBox4 = System.Windows.Forms.TextBox()
		self._textBox5 = System.Windows.Forms.TextBox()
		self._textBox6 = System.Windows.Forms.TextBox()
		self._button1 = System.Windows.Forms.Button()
		self._button2 = System.Windows.Forms.Button()
		self._button3 = System.Windows.Forms.Button()
		self._label4 = System.Windows.Forms.Label()
		self._label5 = System.Windows.Forms.Label()
		self._label6 = System.Windows.Forms.Label()
		self._label7 = System.Windows.Forms.Label()
		self._label8 = System.Windows.Forms.Label()
		self._label9 = System.Windows.Forms.Label()
		self._label10 = System.Windows.Forms.Label()
		self._label11 = System.Windows.Forms.Label()
		self.SuspendLayout()
		# 
		# label1
		# 
		self._label1.BackColor = System.Drawing.Color.PaleTurquoise
		self._label1.Font = System.Drawing.Font("Microsoft Sans Serif", 26.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label1.Location = System.Drawing.Point(55, 10)
		self._label1.Name = "label1"
		self._label1.Size = System.Drawing.Size(555, 150)
		self._label1.TabIndex = 0
		self._label1.Text = "Enter the three runners' names and finishing times."
		self._label1.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label2
		# 
		self._label2.BackColor = System.Drawing.Color.LightSeaGreen
		self._label2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label2.Location = System.Drawing.Point(55, 175)
		self._label2.Name = "label2"
		self._label2.Size = System.Drawing.Size(155, 60)
		self._label2.TabIndex = 1
		self._label2.Text = "Name"
		self._label2.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label3
		# 
		self._label3.BackColor = System.Drawing.Color.LightSeaGreen
		self._label3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label3.Location = System.Drawing.Point(455, 175)
		self._label3.Name = "label3"
		self._label3.Size = System.Drawing.Size(155, 60)
		self._label3.TabIndex = 2
		self._label3.Text = "Finishing time (in seconds)"
		self._label3.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# textBox1
		# 
		self._textBox1.BackColor = System.Drawing.Color.Turquoise
		self._textBox1.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox1.Location = System.Drawing.Point(55, 245)
		self._textBox1.Name = "textBox1"
		self._textBox1.Size = System.Drawing.Size(155, 29)
		self._textBox1.TabIndex = 3
		# 
		# textBox2
		# 
		self._textBox2.BackColor = System.Drawing.Color.Turquoise
		self._textBox2.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox2.Location = System.Drawing.Point(55, 275)
		self._textBox2.Name = "textBox2"
		self._textBox2.Size = System.Drawing.Size(155, 29)
		self._textBox2.TabIndex = 4
		# 
		# textBox3
		# 
		self._textBox3.BackColor = System.Drawing.Color.Turquoise
		self._textBox3.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox3.Location = System.Drawing.Point(55, 305)
		self._textBox3.Name = "textBox3"
		self._textBox3.Size = System.Drawing.Size(155, 29)
		self._textBox3.TabIndex = 5
		self._textBox3.TextChanged += self.TextBox3TextChanged
		# 
		# textBox4
		# 
		self._textBox4.BackColor = System.Drawing.Color.Turquoise
		self._textBox4.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox4.Location = System.Drawing.Point(455, 245)
		self._textBox4.Name = "textBox4"
		self._textBox4.Size = System.Drawing.Size(155, 29)
		self._textBox4.TabIndex = 6
		# 
		# textBox5
		# 
		self._textBox5.BackColor = System.Drawing.Color.Turquoise
		self._textBox5.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox5.Location = System.Drawing.Point(455, 275)
		self._textBox5.Name = "textBox5"
		self._textBox5.Size = System.Drawing.Size(155, 29)
		self._textBox5.TabIndex = 7
		# 
		# textBox6
		# 
		self._textBox6.BackColor = System.Drawing.Color.Turquoise
		self._textBox6.Font = System.Drawing.Font("Microsoft Sans Serif", 14.25, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._textBox6.Location = System.Drawing.Point(455, 305)
		self._textBox6.Name = "textBox6"
		self._textBox6.Size = System.Drawing.Size(155, 29)
		self._textBox6.TabIndex = 8
		# 
		# button1
		# 
		self._button1.BackColor = System.Drawing.Color.DarkCyan
		self._button1.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button1.Location = System.Drawing.Point(55, 600)
		self._button1.Name = "button1"
		self._button1.Size = System.Drawing.Size(155, 70)
		self._button1.TabIndex = 9
		self._button1.Text = "Calculate Race Results"
		self._button1.UseVisualStyleBackColor = False
		self._button1.Click += self.Button1Click
		# 
		# button2
		# 
		self._button2.BackColor = System.Drawing.Color.DarkCyan
		self._button2.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button2.Location = System.Drawing.Point(255, 600)
		self._button2.Name = "button2"
		self._button2.Size = System.Drawing.Size(155, 70)
		self._button2.TabIndex = 10
		self._button2.Text = "Clear"
		self._button2.UseVisualStyleBackColor = False
		self._button2.Click += self.Button2Click
		# 
		# button3
		# 
		self._button3.BackColor = System.Drawing.Color.DarkCyan
		self._button3.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._button3.Location = System.Drawing.Point(455, 600)
		self._button3.Name = "button3"
		self._button3.Size = System.Drawing.Size(155, 70)
		self._button3.TabIndex = 11
		self._button3.Text = "Exit"
		self._button3.UseVisualStyleBackColor = False
		self._button3.Click += self.Button3Click
		# 
		# label4
		# 
		self._label4.BackColor = System.Drawing.Color.DarkCyan
		self._label4.Location = System.Drawing.Point(55, 335)
		self._label4.Name = "label4"
		self._label4.Size = System.Drawing.Size(555, 260)
		self._label4.TabIndex = 12
		# 
		# label5
		# 
		self._label5.BackColor = System.Drawing.Color.LightSeaGreen
		self._label5.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label5.Location = System.Drawing.Point(55, 375)
		self._label5.Name = "label5"
		self._label5.Size = System.Drawing.Size(155, 60)
		self._label5.TabIndex = 13
		self._label5.Text = "First Place"
		self._label5.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label6
		# 
		self._label6.BackColor = System.Drawing.Color.LightSeaGreen
		self._label6.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label6.Location = System.Drawing.Point(55, 435)
		self._label6.Name = "label6"
		self._label6.Size = System.Drawing.Size(155, 60)
		self._label6.TabIndex = 14
		self._label6.Text = "Second Place"
		self._label6.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label7
		# 
		self._label7.BackColor = System.Drawing.Color.LightSeaGreen
		self._label7.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label7.Location = System.Drawing.Point(55, 495)
		self._label7.Name = "label7"
		self._label7.Size = System.Drawing.Size(155, 60)
		self._label7.TabIndex = 15
		self._label7.Text = "Third Place"
		self._label7.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label8
		# 
		self._label8.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label8.Location = System.Drawing.Point(55, 335)
		self._label8.Name = "label8"
		self._label8.Size = System.Drawing.Size(155, 40)
		self._label8.TabIndex = 16
		self._label8.Text = "Race Result"
		self._label8.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label9
		# 
		self._label9.BackColor = System.Drawing.Color.Turquoise
		self._label9.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label9.Location = System.Drawing.Point(355, 375)
		self._label9.Name = "label9"
		self._label9.Size = System.Drawing.Size(155, 60)
		self._label9.TabIndex = 17
		self._label9.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label10
		# 
		self._label10.BackColor = System.Drawing.Color.Turquoise
		self._label10.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label10.Location = System.Drawing.Point(355, 435)
		self._label10.Name = "label10"
		self._label10.Size = System.Drawing.Size(155, 60)
		self._label10.TabIndex = 18
		self._label10.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# label11
		# 
		self._label11.BackColor = System.Drawing.Color.Turquoise
		self._label11.Font = System.Drawing.Font("Microsoft Sans Serif", 15.75, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, 0)
		self._label11.Location = System.Drawing.Point(355, 495)
		self._label11.Name = "label11"
		self._label11.Size = System.Drawing.Size(155, 60)
		self._label11.TabIndex = 19
		self._label11.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.DarkTurquoise
		self.ClientSize = System.Drawing.Size(649, 681)
		self.Controls.Add(self._label11)
		self.Controls.Add(self._label10)
		self.Controls.Add(self._label9)
		self.Controls.Add(self._label8)
		self.Controls.Add(self._label7)
		self.Controls.Add(self._label6)
		self.Controls.Add(self._label5)
		self.Controls.Add(self._label4)
		self.Controls.Add(self._button3)
		self.Controls.Add(self._button2)
		self.Controls.Add(self._button1)
		self.Controls.Add(self._textBox6)
		self.Controls.Add(self._textBox5)
		self.Controls.Add(self._textBox4)
		self.Controls.Add(self._textBox3)
		self.Controls.Add(self._textBox2)
		self.Controls.Add(self._textBox1)
		self.Controls.Add(self._label3)
		self.Controls.Add(self._label2)
		self.Controls.Add(self._label1)
		self.Name = "MainForm"
		self.Text = "RaceRes"
		self.ResumeLayout(False)
		self.PerformLayout()


	def TextBox3TextChanged(self, sender, e):
		pass

	def Button1Click(self, sender, e):
		person1 = str(self._textBox1.Text)
		person2 = str(self._textBox2.Text)
		person3 = str(self._textBox3.Text)
		time1 = int(self._textBox4.Text)
		time2 = int(self._textBox5.Text)
		time3 = int(self._textBox6.Text)
		if time1 < time2 and time3:
			self._label9.Text = str(person1)
			if time2 < time3:
				self._label10.Text = str(person2)
				self._label11.Text = str(person3)
			if time3 < time2:
				self._label10.Text = str(person3)
				self._label11.Text = str(person2)
		if time2 < time1 and time3:
			self._label9.Text = str(person2)
			if time1 < time3:
				self._label10.Text = str(person1)
				self._label11.Text = str(person3)
			if time3 < time1:
				self._label10.Text = str(person3)
				self._label11.Text = str(person1)
		if time3 < time1 and time2:
			self._label9.Text = str(person3)
			if time1 < time2:
				self._label10.Text = str(person1)
				self._label11.Text = str(person2)
			if time2 < time1:
				self._label10.Text = str(person2)
				self._label11.Text = str(person1)

	def Button2Click(self, sender, e):
		self._textBox1.Text = ""
		self._textBox2.Text = ""
		self._textBox3.Text = ""
		self._textBox4.Text = ""
		self._textBox5.Text = ""
		self._textBox6.Text = ""
		self._label9.Text = ""
		self._label10.Text = ""
		self._label11.Text = ""

	def Button3Click(self, sender, e):
		Application.Exit()