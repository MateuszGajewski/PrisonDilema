import Zad1.game
import Zad1.player_betray
import Zad1.player_coop
import Zad1.revenge_player

player_coop = Zad1.player_coop.CoopPlayer()
player_betray = Zad1.player_betray.BetrayPlayer()
revenge_player = Zad1.revenge_player.RevengePlayer()
game = Zad1.game.Game(revenge_player, player_betray, "unknown")
game.play()
