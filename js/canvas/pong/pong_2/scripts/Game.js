const left_counter = document.getElementById("left_counter")
const right_counter = document.getElementById("right_counter")
const color = "#000000"

class Platform {

    static get P() {
        return [0.4, 1]
    }

    static get I() {
        return [0.45 ,1]
    }

    static get D() {
        return [0.1, 0.8]
    }

    static get ACC_MAX() {
        return [100, 500] 
    }

    static get I_MAX() {
        return [100, 1000]
    }

    static get H() {
        return 64
    }

    static get W() {
        return 24
    }

    constructor(pos, ballRef, height, width) {
    this.position = pos
    this.velocity = new Vector2()
    this.ballRef = ballRef
    this.iState = 0
    this.dState = 0
    this.color = color
		this.fieldHeight = height
		this.fieldWidth = width
		this.GameMode = 0
		this.p_speed = 300
		this.b_speed = 300
    }

    keepTarget() {
        const e = (this.ballRef.position.y - 
          (this.position.y + Platform.H / 2))
        const pTerm = Platform.P[this.GameMode] * e
        this.iState = this.iState + e
        this.iState = Math.max( 
          -Platform.I_MAX[this.GameMode],
           Math.min(this.iState, Platform.I_MAX[this.GameMode]))
        const iTerm = Platform.I[this.GameMode] * this.iState

        const dTerm = Platform.D[this.GameMode] * (e - this.dState)
        this.dState = e

        let acc = pTerm + iTerm - dTerm
        acc = Math.max( 
          -Platform.ACC_MAX[this.GameMode],
           Math.min( 
            Platform.ACC_MAX[this.GameMode], 
            acc ))
        this.velocity.y = acc
    }

    update(dt) {
        // if (this.position.y <= 0 ||
        //     this.position.y >= innerHeight - Platform.H) {
        //     this.velocity = new Vector2()
        // }

        this.position = this.position.add(
            this.velocity.mul(dt)
        )

        if (this.position.y <= 0) {
            this.position.y = 0
        }
        if (this.position.y >= this.fieldHeight - Platform.H) {
            this.position.y = this.fieldHeight  - Platform.H
        }
    }

    render(ctx) {
        ctx.fillRect(
            this.position.x,
            this.position.y,
            Platform.W,
            Platform.H
        )
    }

}

class Ball {
    static get R() {
        return 12
    }

    constructor(pos, gameRef, height, width) {
    this.position = pos
    this.velocity = new Vector2(-100, 100)
    this.gameRef = gameRef
		this.speed = 1
		// console.log(this.gameRef)
		this.fieldHeight = height
		this.fieldWidth = width
    }

    update(dt) {
        this.position = this.position.add( this.velocity.mul(dt) )
        this.check()
        this.checkPlatforms()
    }

    render(ctx) {
        ctx.save()
        ctx.fillStyle = '#8B0000'
        ctx.arc( 
          this.position.x, 
          this.position.y, 
          Ball.R, 
          0, 
          2 * Math.PI 
          )
        ctx.fill()
        ctx.restore()
    }

    check() {
        const leftX = this.position.x - Ball.R
        const rightX = this.position.x + Ball.R
        const topY = this.position.y - Ball.R
        const bottomY = this.position.y + Ball.R
        if (bottomY >= this.fieldHeight || topY <= 0) {
            this.velocity.y *= -1
			on_sound('kick.mp3')
        }

        if (rightX < 0) {
            this.gameRef.onGoal(true)
        } else if (leftX > this.fieldWidth) {
            this.gameRef.onGoal(false)
        }
    }

    checkPlatforms() {
        const isRightField = this.position.x > this.fieldWidth / 2
        let pX
        let pY
        let bXo
        if (isRightField) {
            pX = this.gameRef.rightPlatform.position.x + 10
            pY = this.gameRef.rightPlatform.position.y
            bXo = Ball.R
        } else {
            pX = this.gameRef.leftPlatform.position.x + Platform.W
            pY = this.gameRef.leftPlatform.position.y
            bXo = -Ball.R
        }
        const bX = this.position.x + bXo
        const bY = this.position.y
        
        if ( bX >= pX - 10 && 
          bX < pX &&  
          bY >= pY && 
          bY <= pY + Platform.H 
          ) {
            this.velocity.x *= -1
			on_sound('kick.mp3')
        }
    }
}

class Game {
    static get States() {
        return {
            // WELCOME: 1,
            // GAME_PROCESS: 2,
            // GAME_PLAYER_RESPAWN: 3,
            // GAME_OVER: 4
            WELCOME: 1,
            GAME_PROCESS: 2,
            GAME_PLAYER_RESPAWN_LEFT: 3,
			      GAME_PLAYER_RESPAWN_RIGHT: 4,
            GAME_OVER: 5
        }
    }

    static get MaxFPS() {
        return 30
    }

    static get TickLength() {
        return (1 / Game.MaxFPS) * 1000
    }

    constructor(height, width) {
        // Время прошедшего кадра
		this.isBotLeft = true
		// this.isBotRight = false
		this.botCount = 1
        this.lastTick = 0
		this.HEIGHT = height
		this.WIDTH = width
    }

    difficult(value){
			this.leftPlatform.GameMode = value
	}

	ball_speed(value){
		console.log(parseInt(value / this.ball.speed))
		this.ball.velocity.x *= value / this.ball.speed
		this.ball.velocity.y *= value / this.ball.speed
		this.ball.speed=value
		console.log(this.ball.velocity)
	}

	platform_speed(value){
		let speed = 0
		switch (value){
			case 0:
				speed = 200
				break
			case 1:
				speed = 400
				break
			case 2:
				speed = 1000
				break
		}
		this.leftPlatform.p_speed = speed
		this.rightPlatform.p_speed = speed
	}

    // onGoal(isLeft) {
		// const left_target = this.leftPlatform
		// const right_target = this.rightPlatform

		// if (isLeft){
		// 	right_counter.innerHTML = parseInt(right_counter.innerHTML) + 1
    //   on_sound('winner.mp3')
		// } else {
		// 	left_counter.innerHTML = parseInt(left_counter.innerHTML) + 1
    //   on_sound('defeat.mp3')
		// }

		// if (isLeft){
		// 	let x = left_target.position.x
		// 		if (isLeft) {
		// 			x += Platform.W + Ball.R + 5
		// 		} else {
		// 			x -= Ball.R + 5
		// 		}
				
		// 	if (this.isBotLeft){
		// 		this.ball.velocity = Vector2.random(100 * this.ball.speed, 200 * this.ball.speed, -200 * this.ball.speed, 200 * this.ball.speed)
		// 		on_sound('kick.mp3')
		// 	} else {
		// 		left_target.position.y = this.HEIGHT / 2
		// 		this.ball.velocity = new Vector2()
		// 		left_target.velocity = new Vector2()
		// 		this.gameState = Game.States.GAME_PLAYER_RESPAWN
		// 	}
		// 	let y = left_target.position.y + Platform.H / 2
		// 	this.ball.position = new Vector2(x, y)
		// } else {
		// 	let x = right_target.position.x
		// 		if (isLeft) {
		// 			x += Platform.W + Ball.R + 5
		// 		} else {
		// 			x -= Ball.R + 5
		// 		}
					
		// 	// if (this.isBotRight){
		// 	// 	this.ball.velocity = Vector2.random(-100 * this.ball.speed, -200 * this.ball.speed, -200 * this.ball.speed, 200 * this.ball.speed)
		// 	// 	on_sound('kick.mp3')
		// 	// } else {
		// 	// 	right_target.position.y = this.HEIGHT / 2
		// 	// 	this.ball.velocity = new Vector2()
		// 	// 	right_target.velocity = new Vector2()
		// 	// 	this.gameState = Game.States.GAME_PLAYER_RESPAWN
		// 	// }
		// 	let y = right_target.position.y + Platform.H / 2
		// 	this.ball.position = new Vector2(x, y)
		// }
    // }
    onGoal(isLeft) {
      const left_target = this.leftPlatform
      const right_target = this.rightPlatform
  
      if (isLeft){
        right_counter.innerHTML = parseInt(right_counter.innerHTML) + 1
      } else {
        left_counter.innerHTML = parseInt(left_counter.innerHTML) + 1
      }
  
      if (isLeft){
        let x = left_target.position.x
          if (isLeft) {
            x += Platform.W + Ball.R + 5
          } else {
            x -= Ball.R + 5
          }
          
        if (this.isBotLeft){
          this.ball.velocity = Vector2.random(100 * this.ball.speed, 200 * this.ball.speed, -200 * this.ball.speed, 200 * this.ball.speed)
          play_audio('bounce.mp3')
        } else {
          left_target.position.y = this.HEIGHT / 2
          this.ball.velocity = new Vector2()
          left_target.velocity = new Vector2()
          this.gameState = Game.States.GAME_PLAYER_RESPAWN_LEFT
        }
        let y = left_target.position.y + Platform.H / 2
        this.ball.position = new Vector2(x, y)
      } else {
        let x = right_target.position.x
          if (isLeft) {
            x += Platform.W + Ball.R + 5
          } else {
            x -= Ball.R + 5
          }
            
        if (this.isBotRight){
          this.ball.velocity = Vector2.random(-100 * this.ball.speed, -200 * this.ball.speed, -200 * this.ball.speed, 200 * this.ball.speed)
          play_audio('bounce.mp3')
        } else {
          right_target.position.y = this.HEIGHT / 2
          this.ball.velocity = new Vector2()
          right_target.velocity = new Vector2()
          this.gameState = Game.States.GAME_PLAYER_RESPAWN_RIGHT
        }
        let y = right_target.position.y + Platform.H / 2
        this.ball.position = new Vector2(x, y)
      }
      }
  

    onCreate() {
        // this.isBotLeft = false
		this.isBotLeft = true

        this.gameState = Game.States.WELCOME

        this.ball = new Ball( new Vector2( 
          this.WIDTH / 2, 
          this.HEIGHT / 2 ),
          this,
           this.HEIGHT,
            this.WIDTH )

        const OFFSET_H = 40
        this.leftPlatform = new Platform( 
          new Vector2(OFFSET_H, 
            this.HEIGHT / 2 - (Platform.H / 2)), 
            this.ball, 
            this.HEIGHT, 
            this.WIDTH)
        this.rightPlatform = new Platform( 
          new Vector2(this.WIDTH - OFFSET_H - Platform.W, 
            this.HEIGHT / 2 - (Platform.H/ 2)), 
            this.ball, 
            this.HEIGHT, 
            this.WIDTH)

        document.addEventListener('keydown', (e) => this.onInput(e))
        // document.addEventListener('keydown', this.onInput)
       
    }

    onInput(e) {
        // this - Game
        // console.log(e, this);
		const right_target = this.rightPlatform
		const left_target = this.leftPlatform
        switch(e.keyCode) {
            case 32: // SPACE
                if (this.gameState === Game.States.WELCOME) {
                    // Начинаем игру
                    on_sound('start.mp3')
                    this.gameState = Game.States.GAME_PROCESS
                } else if (this.gameState === Game.States.GAME_PLAYER_RESPAWN_LEFT) {
					this.ball.velocity = Vector2.random(
            100 * this.ball.speed, 
            200 * this.ball.speed, 
            -200 * this.ball.speed, 
            200 * this.ball.speed)
					on_sound('kick.mp3')
					this.gameState = Game.States.GAME_PROCESS
          }
          else if (this.gameState === Game.States.GAME_PLAYER_RESPAWN_RIGHT) {
            this.ball.velocity = Vector2.random(-100 * this.ball.speed, -200 * this.ball.speed, -200 * this.ball.speed, 200 * this.ball.speed)
            play_audio('bounce.mp3')
            this.gameState = Game.States.GAME_PROCESS
          }
                break
            case 38: // UP
                if (this.gameState === Game.States.GAME_PROCESS)
					right_target.velocity.y = -right_target.p_speed
                break
            case 40: // DOWN
                if (this.gameState === Game.States.GAME_PROCESS)
					right_target.velocity.y = right_target.p_speed
                break
			case 87: // W
				if (this.isBotLeft)
					break
				if (this.gameState === Game.States.GAME_PROCESS)
					left_target.velocity.y = -left_target.p_speed
                break
			case 83: // S
				if (this.isBotLeft)
					break
				if (this.gameState === Game.States.GAME_PROCESS)
					left_target.velocity.y = left_target.p_speed
                break
        }
    }

    onUpdate(tFrame) {
        // Кол-во секунд, которые прошли с 
        // момента последнего обновления
        const dt = (tFrame - this.lastTick) / 1000
        this.lastTick = tFrame
        // console.log('onUpdate', dt);

        if (this.gameState === Game.States.GAME_PROCESS || 
          this.gameState === Game.States.GAME_PLAYER_RESPAWN_LEFT || 
          this.gameState === Game.States.GAME_PLAYER_RESPAWN_RIGHT) {
            this.leftPlatform.update(dt)
            this.rightPlatform.update(dt)
            this.ball.update(dt)

            if (this.isBotLeft) {
                this.leftPlatform.keepTarget()
            } 
			      else{
				      this.rightPlatform.keepTarget()
			}
        }
    }

    onRender(ctx) {
		ctx.clearRect(0, 0, this.WIDTH, this.HEIGHT)
        ctx.beginPath()
        
        this.leftPlatform.render(ctx, this)
        this.rightPlatform.render(ctx)
        this.ball.render(ctx)

        if (this.gameState === Game.States.WELCOME) {
            ctx.font = '48px ARCADECLASSIC'
            ctx.fillText('Press SPACE to start!', this.WIDTH / 2 - 200, this.HEIGHT / 2)
        }
    }

} 


function on_sound(file){
	let sound = new Audio();
	sound.volume = 0.1
	sound.src = 'sound/' + file;
	sound.autoplay = true;
}

 function changePlayer(){
	  document.activeElement.blur()
		document.getElementById("left_side").innerHTML = game.isBotLeft ? "player" : "bot"
		game.isBotLeft = game.isBotLeft ? false : true
		game.leftPlatform.velocity = new Vector2()
}

function difficult(value){
	game.difficult(value)
}

function ball_speed(value){
	game.ball_speed(value)
}

function platform_speed(value){
	game.platform_speed(value)
}

function showMenu() {
  on_sound('button.mp3')
  document.getElementById('menu').classList.toggle('menu_view');
  if(document.getElementById('menu').classList.contains('menu_view')){
    document.getElementById('menu_start').innerText = "X";
  }
  else{
    document.getElementById('menu_start').innerText = "M";
  }
}
