class Platform {

  static get P() {
    return [0.4, 0.8, 1]//Скорость реакции бота
  }

  static get I() {
    return [0.45, 0.8, 1] //множитель реакции бота
  }

  static get D() {
    return [0.1, 0.3, 0.5]
  }

  static get ACC_MAX() {
    return [100, 150, 200] // Макс. ускорение платформы
  }

  static get I_MAX() {
    return [100, 150, 200] //
  }

  static get H() {
    return 64
  }

  static get W() {
    return 24
  }

  constructor(pos, ballRef) {
    this.position = pos
    this.velocity = new Vector2()
    this.ballRef = ballRef

    this.iState = 0
    this.dState = 0
    this.mode = 0
    this.PLAYER_SPEED = 200
    this.BOT_SPEED = 200
  }

  keepTarget() {
    const e = (this.ballRef.position.y -
      (this.position.y + Platform.H / 2))

    const pTerm = Platform.P * e
    this.iState = this.iState + e
    this.iState = Math.max(
      -Platform.I_MAX[this.mode],
      Math.min(this.iState, Platform.I_MAX[this.mode])
    )
    const iTerm = Platform.I[this.mode] * this.iState

    const dTerm = Platform.D[this.mode] * (e - this.dState)
    this.dState = e

    let acc = pTerm + iTerm - dTerm
    acc = Math.max(
      -Platform.ACC_MAX[this.mode],
      Math.min(
        Platform.ACC_MAX[this.mode],
        acc
      )
    )
    this.velocity.y = acc
  }

  update(dt) {
    this.position = this.position.add(/////////////////////////////////////////////////////////////////////////////////
      this.velocity.mul(dt)
    )

    if (this.position.y <= 0) {
      this.position.y = 0
    }
    if (this.position.y >= innerHeight - Platform.H) {
      this.position.y = innerHeight - Platform.H
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

  constructor(pos, gameRef) {
    this.position = pos
    this.velocity = new Vector2(-100, 100)
    this.gameRef = gameRef
    this.gameRef = gameRef
    this.speed = 1
  }

  update(dt) {
    this.position = this.position.add(
      this.velocity.mul(dt)
    )
    this.check()
    this.checkPlatforms()
  }

  render(ctx) {
    ctx.save()
    ctx.fillStyle = '#33b5e5'
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
    if (bottomY >= innerHeight || topY <= 0) {
      this.velocity.y *= -1
      console.log('pip')
    }

    if (rightX < 0) {
      this.gameRef.onGoal(true)
    } else if (leftX > innerWidth) {
      this.gameRef.onGoal(false)
    }
  }

  checkPlatforms() {
    const isRightField = this.position.x > innerWidth / 2
    let pX
    let pY
    let bXo // Смещение от центра шарика
    if (isRightField) {
      // Проверка с правой платформой
      pX = this.gameRef.rightPlatform.position.x + 10
      pY = this.gameRef.rightPlatform.position.y
      bXo = Ball.R
    } else {
      // Левая платформа
      pX = this.gameRef.leftPlatform.position.x
        + Platform.W
      pY = this.gameRef.leftPlatform.position.y
      bXo = -Ball.R
    }
    const bX = this.position.x + bXo
    const bY = this.position.y

    if (
      bX >= pX - 10 &&
      bX < pX &&
      bY >= pY &&
      bY <= pY + Platform.H
    ) {
      this.velocity.x *= -1/////////////////////////////////////////////////////////////////////
    }
  }
}

class Game {

  static get States() {
    return {
      WELCOME: 1,
      GAME_PROCESS: 2,
      GAME_PLAYER_RESPAWN: 3,
      GAME_PLAYER_RESPAWN_RIGHT: 4,
      GAME_OVER: 4
    }
  }

  static get MaxFPS() {
    return 30
  }

  static get TickLength() {
    return (1 / Game.MaxFPS) * 1000
  }

  constructor() {
    // Время прошедшего кадра
    this.lastTick = 0
    this.botCount = 1
    // this.HEIGHT = height
    // this.WIDTH = width
  }

  onGoal(isLeft) {//////////////////////////////////////////////////////////////////////////
    const target = isLeft ? this.leftPlatform : this.rightPlatform

    let x = target.position.x
    if (isLeft) {
      x += Platform.W + Ball.R + 5
    } else {
      x -= Ball.R + 5
    }

    let y = target.position.y + Platform.H / 2
    this.ball.position = new Vector2(x, y)

    if ((isLeft && this.isBotLeft) || (!isLeft && !this.isBotLeft)) {
      // Проиграл бот.
      if (isLeft) {
        this.ball.velocity = Vector2.random(100, 200, -200, 200)
      } else {
        this.ball.velocity = Vector2.random(-200, -100, -200, 200)
      }
      console.log('Bot failed', isLeft);
    } else {
      // Проиграл игрок.
      this.ball.velocity = new Vector2()
      target.velocity = new Vector2()
      this.gameState = Game.States.GAME_PLAYER_RESPAWN
    }
  }

  onCreate() {
    this.isBotLeft = false

    this.gameState = Game.States.WELCOME

    this.ball = new Ball(
      new Vector2(
        innerWidth / 2,
        innerHeight / 2
      ),
      this
    )

    const OFFSET_H = 40
    this.leftPlatform = new Platform(
      new Vector2(OFFSET_H,
        window.innerHeight / 2 - (Platform.H / 2)
      ), this.ball)
    this.rightPlatform = new Platform(
      new Vector2(innerWidth - OFFSET_H - Platform.W,
        window.innerHeight / 2 - (Platform.H / 2)
      ),
      this.ball
    )

    document.addEventListener('keydown', (e) => this.onInput(e))
    // document.addEventListener('keydown', this.onInput)
  }

  onInput(e) {////////////////////////////////////////////////////////////////////////////////////////
    // this - Game
    // console.log(e, this);
    const target = this.isBotLeft ? this.rightPlatform : this.leftPlatform
    switch (e.keyCode) {
      case 32: // SPACE
        if (this.gameState === Game.States.WELCOME) {
          // Начинаем игру
          this.gameState = Game.States.GAME_PROCESS
        } else if (this.gameState === Game.States.GAME_PLAYER_RESPAWN) {
          // Только при проигрыше игрока
          if (target.isBotLeft) {
            // Игрок справа
            // this.ball.velocity = Vector2.random(-200, -100, -200, 200)
            this.ball.velocity = Vector2.random(100 * this.ball.speed, 200 * this.ball.speed, -200 * this.ball.speed, 200 * this.ball.speed)
          } else {
            // Игрок слева
            // this.ball.velocity = Vector2.random(100, 200, -200, 200)
            this.ball.velocity = Vector2.random(-100 * this.ball.speed, -200 * this.ball.speed, -200 * this.ball.speed, 200 * this.ball.speed)
          }
          this.gameState = Game.States.GAME_PROCESS
        }
        break
      case 38: // UP
        if (this.gameState === Game.States.GAME_PROCESS)
          target.velocity.y = -200
        break
      case 40: // DOWN
        if (this.gameState === Game.States.GAME_PROCESS)
          target.velocity.y = 200
        break
      case 87: // W
        if (this.isBotLeft)
          break
        if (this.gameState === Game.States.GAME_PROCESS)
          left_target.velocity.y = -left_target.PLAYER_SPEED
        break
      case 83: // S
        if (this.isBotLeft)
          break
        if (this.gameState === Game.States.GAME_PROCESS)
          left_target.velocity.y = left_target.PLAYER_SPEED
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
      this.gameState === Game.States.GAME_PLAYER_RESPAWN) {
      this.leftPlatform.update(dt)
      this.rightPlatform.update(dt)
      this.ball.update(dt)

      if (this.isBotLeft) {
        this.leftPlatform.keepTarget()
      } else {
        this.rightPlatform.keepTarget()
      }
    }
  }

  onRender(ctx) {
    ctx.clearRect(0, 0,
      window.innerWidth, window.innerHeight)
    ctx.beginPath()

    this.leftPlatform.render(ctx)
    this.rightPlatform.render(ctx)
    this.ball.render(ctx)

    if (this.gameState === Game.States.WELCOME) {
      ctx.font = '48px serif'
      ctx.fillText('Press SPACE to start!', innerWidth / 2 - 200,
        innerHeight / 2)
    }
  }

} 
