from src.casinobuild import casino, ceils
from src import simulator, log, preparation
from src.chips import chips_nominals

def main() -> None:
    log.make_log()
    print("======= ИНИЦИАЛИЗАЦИЯ СТАРТОВЫХ ДАННЫХ =======\n")
    # ОПРЕДЕЛЕНИЕ ЦВЕТОВ И НОМИНАЛОВ ФИШЕК
    CHIPS = chips_nominals.ChipNominals()
    preparation.CreateChips(CHIPS)

    # СОЗДАНИЕ ЯЧЕЕК
    CEILS = ceils.CEILS()
    preparation.CreateCeils(CEILS)

    Casino = casino.Casino(CHIPS=CHIPS, CEILS=CEILS)
    Casino.RenewCasinoBalance(10_000)
    Simulator = simulator.Simulation(casino=Casino)

    # СОЗДАНИЕ СТАРТОВОГО НАБОРА ИГРОКОВ
    print("-----СОЗДАНИЕ СТАРТОВОГ НАБОРА ИГРОКОВ-----")
    preparation.AddPlayers(Simulator)
    print("\n\n")

    print("-----СОЗДАНИЕ СТАРТОВОГО НАБОРА ГУСЕЙ-----")
    # ГЕНЕРАЦИЯ ГУСЕЙ
    preparation.AddGeese(Simulator)
    print("\n\n")

    # ЗАКУПКА ФИШКАМИ ДЛЯ ИГРОКОВ
    print("-----ЗАКУПКА ФИШЕК ИГРОКАМИ-----")
    preparation.PlayersBuyChips(Simulator, players=Casino.PlayersCollection)
    print("\n\n")

    print("\n======= СТАРТ СИМУЛЯЦИИ =======\n")
    print('-----Задать последовательность? y/n')
    answer = input().strip()
    if answer=='y':
        print("Задайте последовательность")
        seed = input().strip()
    else:
        seed = None 
    
    print('-----Задайте количество шагов-----')
    steps = int(input())

    Simulator.run_simulation(steps=steps, seed=seed)

    # 
if __name__ == "__main__":
    main()