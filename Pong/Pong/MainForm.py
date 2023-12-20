﻿import System.Drawing
import System.Windows.Forms

from System.Drawing import *
from System.Windows.Forms import *

class MainForm(Form):
	def __init__(self):
		self.InitializeComponent()
		self.R = System.Random()
		self.ballup = 0
		self.balld = 0
		self.flagleft = False
		self.flagright = False
	
	def InitializeComponent(self):
		self._components = System.ComponentModel.Container()
		self._lbltitle = System.Windows.Forms.Label()
		self._leftscore = System.Windows.Forms.Label()
		self._rightscore = System.Windows.Forms.Label()
		self._lblball = System.Windows.Forms.Label()
		self._lblleft = System.Windows.Forms.Label()
		self._lblright = System.Windows.Forms.Label()
		self._timerright = System.Windows.Forms.Timer(self._components)
		self._timerleft = System.Windows.Forms.Timer(self._components)
		self._timerball = System.Windows.Forms.Timer(self._components)
		self._timermulti = System.Windows.Forms.Timer(self._components)
		self._timerdummy = System.Windows.Forms.Timer(self._components)
		self._timerboolean = System.Windows.Forms.Timer(self._components)
		self.SuspendLayout()
		# 
		# lbltitle
		# 
		self._lbltitle.BackColor = System.Drawing.Color.Transparent
		self._lbltitle.Font = System.Drawing.Font("Microsoft Sans Serif", 20, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._lbltitle.ForeColor = System.Drawing.Color.White
		self._lbltitle.Location = System.Drawing.Point(12, 25)
		self._lbltitle.Name = "lbltitle"
		self._lbltitle.Size = System.Drawing.Size(958, 52)
		self._lbltitle.TabIndex = 0
		self._lbltitle.Text = "Press Enter to Start or M to start multiplayer"
		self._lbltitle.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		# 
		# leftscore
		# 
		self._leftscore.BackColor = System.Drawing.Color.Transparent
		self._leftscore.Font = System.Drawing.Font("Microsoft Sans Serif", 48, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._leftscore.ForeColor = System.Drawing.Color.White
		self._leftscore.Location = System.Drawing.Point(78, 96)
		self._leftscore.Name = "leftscore"
		self._leftscore.Size = System.Drawing.Size(166, 109)
		self._leftscore.TabIndex = 1
		self._leftscore.Text = "0"
		self._leftscore.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._leftscore.Click += self.LeftscoreClick
		# 
		# rightscore
		# 
		self._rightscore.BackColor = System.Drawing.Color.Transparent
		self._rightscore.Font = System.Drawing.Font("Microsoft Sans Serif", 48, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, 0)
		self._rightscore.ForeColor = System.Drawing.Color.White
		self._rightscore.Location = System.Drawing.Point(734, 96)
		self._rightscore.Name = "rightscore"
		self._rightscore.Size = System.Drawing.Size(166, 109)
		self._rightscore.TabIndex = 2
		self._rightscore.Text = "0"
		self._rightscore.TextAlign = System.Drawing.ContentAlignment.MiddleCenter
		self._rightscore.Click += self.RightscoreClick
		# 
		# lblball
		# 
		self._lblball.BackColor = System.Drawing.Color.White
		self._lblball.Location = System.Drawing.Point(479, 304)
		self._lblball.Name = "lblball"
		self._lblball.Size = System.Drawing.Size(30, 30)
		self._lblball.TabIndex = 3
		self._lblball.Click += self.LblballClick
		# 
		# lblleft
		# 
		self._lblleft.BackColor = System.Drawing.Color.White
		self._lblleft.Location = System.Drawing.Point(12, 246)
		self._lblleft.Name = "lblleft"
		self._lblleft.Size = System.Drawing.Size(20, 100)
		self._lblleft.TabIndex = 4
		# 
		# lblright
		# 
		self._lblright.BackColor = System.Drawing.Color.White
		self._lblright.Location = System.Drawing.Point(950, 246)
		self._lblright.Name = "lblright"
		self._lblright.Size = System.Drawing.Size(20, 100)
		self._lblright.TabIndex = 5
		# 
		# timerright
		# 
		self._timerright.Interval = 20
		self._timerright.Tick += self.TimerrightTick
		# 
		# timerleft
		# 
		self._timerleft.Interval = 20
		self._timerleft.Tick += self.TimerleftTick
		# 
		# timerball
		# 
		self._timerball.Interval = 20
		self._timerball.Tick += self.TimerballTick
		# 
		# timermulti
		# 
		self._timermulti.Interval = 20
		# 
		# timerdummy
		# 
		self._timerdummy.Interval = 10000
		# 
		# MainForm
		# 
		self.BackColor = System.Drawing.Color.Black
		self.ClientSize = System.Drawing.Size(982, 590)
		self.Controls.Add(self._lblball)
		self.Controls.Add(self._lblright)
		self.Controls.Add(self._lblleft)
		self.Controls.Add(self._rightscore)
		self.Controls.Add(self._leftscore)
		self.Controls.Add(self._lbltitle)
		self.Name = "MainForm"
		self.Text = "Pong"
		self.Load += self.MainFormLoad
		self.SizeChanged += self.MainFormSizeChanged
		self.KeyDown += self.MainFormKeyDown
		self.ResumeLayout(False)


	def TimerballTick(self, sender, e):
		ball = self._lblball
		lpdl = self._lblleft
		rpdl = self._lblright
		rscore = int(self._rightscore.Text)
		lscore = int(self._leftscore.Text)
		ball.Top += self.ballup
		ball.Left += 8 * self.balld
		
		if ball.Right >= rpdl.Left and ball.Bottom >= rpdl.Top and ball.Top <= rpdl.Bottom:
			self.balld = -1
			self.ballup = self.R.Next(-4, 5)
		elif ball.Left <= lpdl.Right and ball.Bottom >= lpdl.Top and ball.Top <= lpdl.Bottom:
			self.balld = 1
			self.ballup = self.R.Next(-4, 5)
		
		if ball.Top <= 0:
			self.balld = -1
			ball.Top += 5 * self.balld
		
		if ball.Bottom >= self.Height:
			self.balld = 1
			ball.Top += 5 * self.balld
		
		if ball.Location.X <= 0 or \
		   (ball.Location.X < lpdl.Left + 20 and ball.Location.Y < lpdl.Top):
		   	""" TODO: FINISH LEFT BOUNDARY """
		   	pass
		
		if ball.Location.X >= self.Width or \
		   (ball.Location.X > rpdl.Right + 20 and ball.Location.Y > rpdl.Top):
		   	lscore += 1
		   	ball.Left = self.Width // 2
		   	ball.Top = self.Height // 2
		   	self._leftscore.Text = str(lscore)

		if ball.Location.X >= self.Width or \
		   (ball.Location.X < lpdl.Right - 20 and ball.Location.Y > lpdl.Top):
		   	rscore += 1
		   	ball.Left = self.Width // 2
		   	ball.Top = self.Height // 2
		   	self._rightscore.Text = str(rscore)
		
		""" TODO: FINISH RIGHT SCORE WIN CONDITION """
		
		if lscore == 10:  # Left win condition
			self._timerball.Enabled = False
			ball.Left = self.Width // 2
			ball.Top = self.Height // 2
			self.ballup = 0
			self._lbltitle.Visible = True
			self._lbltitle.Text = "Left Player Wins! Press R to restart"
		
		if rscore == 10:  # Right win condition
			self._timerball.Enabled = False
			ball.Left = self.Width // 2
			ball.Top = self.Height // 2
			self.ballup = 0
			self._lbltitle.Visible = True
			self._lbltitle.Text = "Right Player Wins! Press R to restart"
		
		if ball.Top <= 0:
			self.ballup *= -1
		elif ball.Bottom >= self.Height:
			self.ballup *= -1
		
		if ball.Top <= self.Top:
			self.ballup = 1
		elif ball.Top >= self.Height:
			self.ballup = -1
		rnd = System.Random()
		""" TODO: ? """
		if self._timerboolean.Enabled == True:
			lpdl.Top = ball.Top

	def MainFormKeyDown(self, sender, e):
		tball = self._timerball
		tdum = self._timerdummy
		tbool = self._timerboolean
		tmult = self._timermulti
		tleft = self._timerleft
		tright = self._timerright
		bl = self._lblball
		lblf = self._lblleft
		lblrt = self._lblright
		
		def reset():
			self._lbltitle.Visible = True
			self._lbltitle.Text = "Press Enter to Start or M to start Multiplayer"
			self._leftscore.Text = "0"
			self._rightscore.Text = "0"
			tball.Enabled = False
			tdum.Enabled = False
			tbool.Enabled = False
			tmult.Enabled = False
			tleft.Enabled = False
			tright.Enabled = False
			bl.Left = self.Width // 2
			bl.Top = self.Height // 2
			lblf.Top = (self.Height // 2) - 100 + self._lblleft.Height
			lblrt.Top = (self.Height // 2) - 100 + self._lblright.Height
			""" TODO: RESET SECRETS """
			bl.BackColor = Color.White
			self._lblball.BackColor = Color.White
			self.BackColor = Color.Black
			self._rightscore.ForeColor = Color.White
			self._leftscore.ForeColor = Color.White
			self._lbltitle.ForeColor = Color.White
			self._lblleft.BackColor = Color.White
			self._lblright.BackColor = Color.White
		if e.KeyCode == Keys.R:
			reset()
		
		""" TODO: SECRET CONTROL """
		
		if e.KeyCode == Keys.Enter:
			tball.Enabled = True
			tdum.Enabled = True
			tbool.Enabled = True
			self._lbltitle.Visible = False
		
		if e.KeyCode == Keys.M:
			reset()
			self._lbltitle.Visible = True
			self._lbltitle.Text = "Use W and S to move the left paddle; " \
								  "hit Enter to begin"
			tmult.Enabled = True
			if e.KeyCode == Keys.Enter:
				self._lbltitle.Visible = False
				tbool.Enabled = False
				tmult.Enabled = True
				tdum.Enabled = Ture
				tball.Enabled = True
		
		if tdum.Enabled:
			if e.KeyCode == Keys.Up:
				self.flagright = False
				tright.Enabled = True
			elif e.KeyCode == Keys.Down:
				self.flagright = True
				tright.Enabled = True
			elif tright.Enabled and self.flagright == False:
				tright.Enabled = False
		
		""" TODO: FINISH MULTIPLAYER CONTROLS """
		if tmult.Enabled and tball.Enabled:
			""" FOR BOTH KEYS, ALSO NEED TO SET tbool.Enabled = False """
			if e.KeyCode == Keys.W:
				self.flagleft = True
				tleft.Enabled = True
			elif e.KeyCode == Keys.S:
				self.flagleft = True
				tleft.Enabled = True
			elif tleft.Enabled and self.flagleft == False:
				tleft.Enabled = True 
				
		if e.KeyCode == Keys.O:
			rscore = int(self._rightscore.Text)
			rscore += 1
			self._rightscore.Text = str(rscore)
			if rscore >= 1:
				self._lbltitle.Text = "Good Job!"
				self._lbltitle.ForeColor = Color.White
				self._lbltitle.BackColor = Color.Transparent
				self._lbltitle.Visible = True
			if rscore >= 5:
				self._lbltitle.Text = "Woah There Calm Down!"
				self._lbltitle.ForeColor = Color.White
				self._lbltitle.BackColor = Color.Transparent
			if rscore > 10:
				self._lbltitle.Text = "Cheating is Not Good!"
				self._lblball.BackColor = Color.Black
				self.BackColor = Color.White
				self._rightscore.ForeColor = Color.Black
				self._leftscore.ForeColor = Color.Black
				self._lbltitle.ForeColor = Color.Black
				self._lblleft.BackColor = Color.Black
				self._lblright.BackColor = Color.Black
			if rscore >= 20:
				self._lbltitle.Text = "Are You Still Going?"
				self._lblball.BackColor = Color.Red
				self.BackColor = Color.Green
				self._rightscore.ForeColor = Color.Red
				self._leftscore.ForeColor = Color.Red
				self._lbltitle.ForeColor = Color.Red
				self._lblleft.BackColor = Color.Red
				self._lblright.BackColor = Color.Red
			if rscore >= 30:
				self._lbltitle.Text = "Maybe You Should Stop!"
				self._lblball.BackColor = Color.Orange
				self.BackColor = Color.Blue
				self._rightscore.ForeColor = Color.Orange
				self._leftscore.ForeColor = Color.Orange
				self._lbltitle.ForeColor = Color.Orange
				self._lblleft.BackColor = Color.Orange
				self._lblright.BackColor = Color.Orange
			if rscore >= 40:
				self._lbltitle.Text = "Is It That Serious To You?"
				self._lblball.BackColor = Color.Yellow
				self.BackColor = Color.Purple
				self._rightscore.ForeColor = Color.Yellow
				self._leftscore.ForeColor = Color.Yellow
				self._lbltitle.ForeColor = Color.Yellow
				self._lblleft.BackColor = Color.Yellow
				self._lblright.BackColor = Color.Yellow
			if rscore >= 50:
				self._lbltitle.Text = "What More Do You Want!"
				self._lblball.BackColor = Color.Green
				self.BackColor = Color.Red
				self._rightscore.ForeColor = Color.Green
				self._leftscore.ForeColor = Color.Green
				self._lbltitle.ForeColor = Color.Green
				self._lblleft.BackColor = Color.Green
				self._lblright.BackColor = Color.Green
			if rscore >= 60:
				self._lbltitle.Text = "You're Done Now Right?"
				self._lblball.BackColor = Color.Blue
				self.BackColor = Color.Orange
				self._rightscore.ForeColor = Color.Blue
				self._leftscore.ForeColor = Color.Blue
				self._lbltitle.ForeColor = Color.Blue
				self._lblleft.BackColor = Color.Blue
				self._lblright.BackColor = Color.Blue
			if rscore >= 70:
				self._lbltitle.Text = "Enough!"
				self._lblball.BackColor = Color.Purple
				self.BackColor = Color.Yellow
				self._rightscore.ForeColor = Color.Purple
				self._leftscore.ForeColor = Color.Purple
				self._lbltitle.ForeColor = Color.Purple
				self._lblleft.BackColor = Color.Purple
				self._lblright.BackColor = Color.Purple
			if rscore >= 80:
				self._lbltitle.Text = "No More!"
				self._lblball.BackColor = Color.Black
				self.BackColor = Color.White
				self._rightscore.ForeColor = Color.Black
				self._leftscore.ForeColor = Color.Black
				self._lbltitle.ForeColor = Color.Black
				self._lblleft.BackColor = Color.Black
				self._lblright.BackColor = Color.Black
				self._rightscore.Text = "0"
					
		if e.KeyCode == Keys.L:
			lscore = int(self._leftscore.Text)
			lscore -= 1
			self._leftscore.Text = str(lscore)
			if lscore == -1:
				self._lbltitle.Text = "?!?!?"
				self._lbltitle.Visible = True
			if lscore == -250:
				self._lbltitle.Text = "What Is Happening??"
			if lscore == -500:
				self._lbltitle.Text = "How Are You Doing This!!"
			if lscore == -999:
				self._lbltitle.Text = "Done?!?!?ll"
	def MainFormLoad(self, sender, e):
		""" TODO: ADD 3 UNIQUE SECRETS/CHEATS/EASTER EGGS IN TOTAL
		AND FINISH MULTIPLAYER AND SCOREBOARD AND DUMMY AI """
		self.balld = 1
		self.ballup = self.R.Next(-4, 5)
		self._timerball.Enabled = False
		self._timerdummy.Enabled = False
		self._timermulti.Enabled = False
	
	def pdlTick(self, pdl, flagd, tmr):
		if flagd == True:
			pdl.Top += 5
		if flagd == False:
			pdl.Top -= 5
		if pdl.Top <= 10:
			tmr.Enabled = False
		if pdl.Bottom >= self.Height - 50:
			tmr.Enabled = False

	def TimerleftTick(self, sender, e):
		self.pdlTick(self._lblleft, self.flagleft, self._timerleft)

	def TimerrightTick(self, sender, e):
		self.pdlTick(self._lblright, self.flagright, self._timerright)

	def LblballClick(self, sender, e):
		self._lblball.BackColor = Color.Red
		""" TODO: PUT MORE EASTER EGGS LATER """
		self.BackColor = Color.Green

	def MainFormSizeChanged(self, sender, e):
		self._lblright.Left = self.Width - 25 - self._lblright.Width
		self._lblball.Left = self.Width // 2
		self._lblball.Top = self.Height // 2
		self._lbltitle.Width = self.Width - 25
		self._rightscore.Left = self.Width - 75 - self._rightscore.Width

	def LeftscoreClick(self, sender, e):
		pass
	def RightscoreClick(self, sender, e):
		rscore = int(self._rightscore.Text)
		rscore += 1
		self._rightscore.Text = str(rscore)
		if rscore >= 1:
			self._lbltitle.Text = "Good Job!"
			self._lbltitle.ForeColor = Color.White
			self._lbltitle.BackColor = Color.Transparent
			self._lbltitle.Visible = True
		if rscore >= 5:
			self._lbltitle.Text = "Woah There Calm Down!"
			self._lbltitle.ForeColor = Color.White
			self._lbltitle.BackColor = Color.Transparent
		if rscore > 10:
			self._lbltitle.Text = "Cheating is Not Good!"
			self._lblball.BackColor = Color.Black
			self.BackColor = Color.White
			self._rightscore.ForeColor = Color.Black
			self._leftscore.ForeColor = Color.Black
			self._lbltitle.ForeColor = Color.Black
			self._lblleft.BackColor = Color.Black
			self._lblright.BackColor = Color.Black
		if rscore >= 20:
			self._lbltitle.Text = "Are You Still Going?"
			self._lblball.BackColor = Color.Red
			self.BackColor = Color.Green
			self._rightscore.ForeColor = Color.Red
			self._leftscore.ForeColor = Color.Red
			self._lbltitle.ForeColor = Color.Red
			self._lblleft.BackColor = Color.Red
			self._lblright.BackColor = Color.Red
		if rscore >= 30:
			self._lbltitle.Text = "Maybe You Should Stop!"
			self._lblball.BackColor = Color.Orange
			self.BackColor = Color.Blue
			self._rightscore.ForeColor = Color.Orange
			self._leftscore.ForeColor = Color.Orange
			self._lbltitle.ForeColor = Color.Orange
			self._lblleft.BackColor = Color.Orange
			self._lblright.BackColor = Color.Orange
		if rscore >= 40:
			self._lbltitle.Text = "Is It That Serious To You?"
			self._lblball.BackColor = Color.Yellow
			self.BackColor = Color.Purple
			self._rightscore.ForeColor = Color.Yellow
			self._leftscore.ForeColor = Color.Yellow
			self._lbltitle.ForeColor = Color.Yellow
			self._lblleft.BackColor = Color.Yellow
			self._lblright.BackColor = Color.Yellow
		if rscore >= 50:
			self._lbltitle.Text = "What More Do You Want!"
			self._lblball.BackColor = Color.Green
			self.BackColor = Color.Red
			self._rightscore.ForeColor = Color.Green
			self._leftscore.ForeColor = Color.Green
			self._lbltitle.ForeColor = Color.Green
			self._lblleft.BackColor = Color.Green
			self._lblright.BackColor = Color.Green
		if rscore >= 60:
			self._lbltitle.Text = "You're Done Now Right?"
			self._lblball.BackColor = Color.Blue
			self.BackColor = Color.Orange
			self._rightscore.ForeColor = Color.Blue
			self._leftscore.ForeColor = Color.Blue
			self._lbltitle.ForeColor = Color.Blue
			self._lblleft.BackColor = Color.Blue
			self._lblright.BackColor = Color.Blue
		if rscore >= 70:
			self._lbltitle.Text = "Enough!"
			self._lblball.BackColor = Color.Purple
			self.BackColor = Color.Yellow
			self._rightscore.ForeColor = Color.Purple
			self._leftscore.ForeColor = Color.Purple
			self._lbltitle.ForeColor = Color.Purple
			self._lblleft.BackColor = Color.Purple
			self._lblright.BackColor = Color.Purple
		if rscore == 80:
			self._lbltitle.Text = "No More!"
			self._lblball.BackColor = Color.Black
			self.BackColor = Color.White
			self._rightscore.ForeColor = Color.Black
			self._leftscore.ForeColor = Color.Black
			self._lbltitle.ForeColor = Color.Black
			self._lblleft.BackColor = Color.Black
			self._lblright.BackColor = Color.Black
			self._rscore.Text = "0"