import math


class TournamentModel:
    """
    一个用于模拟和计算英雄联盟线上赛事成本和费用的模型。

    这个类封装了赛事结构、比赛场次、成本预算和多种收费方案的计算逻辑。
    所有计算均基于12支队伍，每队7人的设定。

    方法:
    - get_match_and_game_summary(): 获取比赛场次和游戏局数的详细分析。
    - get_cost_analysis(): 获取赛事的最低成本和期望成本分析。
    - calculate_fee_models(cost_multiplier=1.5): 计算并返回多种收费方案。
    """

    def __init__(self, num_teams: int = 12, players_per_team: int = 7):
        """
        初始化赛事模型的基本参数。

        Args:
            num_teams (int): 参赛队伍数量。
            players_per_team (int): 每支队伍的平均人数。
        """
        # 基本参数
        self.num_teams = num_teams
        self.players_per_team = players_per_team
        self.total_players = num_teams * players_per_team

        # 薪酬配置 (每局BO1)
        self.bo3_config = {'commentators': 2, 'directors': 1}
        self.bo3_salaries = {'commentator': 5, 'director': 6}

        self.bo5_config = {'commentators': 3, 'directors': 2}
        self.bo5_salaries = {'commentator': 5, 'director': 6}

        # 游戏局数期望值
        self.E_BO3 = 2.5
        self.MIN_BO3_GAMES = 2
        self.E_BO5 = 4.125
        self.MIN_BO5_GAMES = 3

        # 执行核心计算
        self._calculate_all()

    def _calculate_all(self):
        """私有方法，执行所有核心计算。"""
        # 1. 计算各阶段对局数
        # 阶段一 (擂台赛)
        main_gauntlet_matches = self.num_teams - 1
        # 假设：整个阶段出现一次3连胜，触发一次强制休息附加赛
        rest_rule_matches = 1
        # 假设：11支败者队(10挑战+1守擂)进入复活赛单败淘汰
        resurrection_bracket_matches = (self.num_teams - 1)
        resurrection_final_match = 1
        self.matches_phase1 = main_gauntlet_matches + rest_rule_matches + resurrection_bracket_matches + resurrection_final_match

        # 阶段二 (淘汰赛)
        group_size = self.num_teams // 2
        group_a_matches = group_size - 1
        group_b_matches = group_size - 1
        self.matches_phase2 = group_a_matches + group_b_matches

        # 2. 计算各阶段BO1局数 (最低和期望)
        self.min_games_phase1 = self.matches_phase1 * self.MIN_BO3_GAMES
        self.expected_games_phase1 = self.matches_phase1 * self.E_BO3

        self.min_games_phase2 = self.matches_phase2 * self.MIN_BO5_GAMES
        self.expected_games_phase2 = self.matches_phase2 * self.E_BO5

        # 3. 计算成本
        self.cost_per_bo3_game = (self.bo3_config['commentators'] * self.bo3_salaries['commentator'] +
                                  self.bo3_config['directors'] * self.bo3_salaries['director'])

        self.cost_per_bo5_game = (self.bo5_config['commentators'] * self.bo5_salaries['commentator'] +
                                  self.bo5_config['directors'] * self.bo5_salaries['director'])

        self.min_cost_phase1 = self.min_games_phase1 * self.cost_per_bo3_game
        self.min_cost_phase2 = self.min_games_phase2 * self.cost_per_bo5_game
        self.min_total_cost = self.min_cost_phase1 + self.min_cost_phase2

        self.expected_cost_phase1 = self.expected_games_phase1 * self.cost_per_bo3_game
        self.expected_cost_phase2 = self.expected_games_phase2 * self.cost_per_bo5_game
        self.expected_total_cost = self.expected_cost_phase1 + self.expected_cost_phase2

    def get_match_and_game_summary(self) -> dict:
        """
        返回比赛场次和游戏局数的详细分析。

        Returns:
            dict: 包含各阶段对局数和BO1局数（最低及期望）的字典。
        """
        return {
            "阶段一对局数 (BO3)": self.matches_phase1,
            "阶段二对局数 (BO5)": self.matches_phase2,
            "总对局数": self.matches_phase1 + self.matches_phase2,
            "阶段一最低BO1局数": self.min_games_phase1,
            "阶段一期望BO1局数": self.expected_games_phase1,
            "阶段二最低BO1局数": self.min_games_phase2,
            "阶段二期望BO1局数": self.expected_games_phase2,
            "赛事总最低BO1局数": self.min_games_phase1 + self.min_games_phase2,
            "赛事总期望BO1局数": self.expected_games_phase1 + self.expected_games_phase2
        }

    def get_cost_analysis(self) -> dict:
        """
        返回赛事的最低成本和期望成本分析。

        Returns:
            dict: 包含各阶段及总成本（最低及期望）的字典。
        """
        return {
            "每局BO3成本": self.cost_per_bo3_game,
            "每局BO5成本": self.cost_per_bo5_game,
            "最低总成本": self.min_total_cost,
            "期望总成本": self.expected_total_cost,
            "详情": {
                "阶段一最低成本": self.min_cost_phase1,
                "阶段二最低成本": self.min_cost_phase2,
                "阶段一期望成本": self.expected_cost_phase1,
                "阶段二期望成本": self.expected_cost_phase2
            }
        }

    def calculate_fee_models(self, cost_multiplier: float = 1.5) -> dict:
        """
        根据最低成本和指定的乘数计算多种收费方案。

        Args:
            cost_multiplier (float): 用于计算最终预算的保守乘数，默认为1.5。

        Returns:
            dict: 包含目标预算和三种不同收费方案的字典。
        """
        target_budget = self.min_total_cost * cost_multiplier

        models = {}

        # 方案A: 均衡模式 (50%个人, 50%团队)
        player_share_a = target_budget * 0.5
        team_share_a = target_budget * 0.5
        models['均衡模式'] = {
            '选手报名费(元/人)': round(player_share_a / self.total_players),
            '队伍建队费(元/队)': round(team_share_a / self.num_teams),
            '说明': '总费用在个人和团队间平均分摊，最公平且易于接受。'
        }

        # 方案B: 团队激励模式 (25%个人, 75%团队)
        player_share_b = target_budget * 0.25
        team_share_b = target_budget * 0.75
        models['团队激励模式'] = {
            '选手报名费(元/人)': round(player_share_b / self.total_players),
            '队伍建队费(元/队)': round(team_share_b / self.num_teams),
            '说明': '降低个人报名门槛，鼓励以团队为单位报名。'
        }

        # 方案C: 个人责任模式 (75%个人, 25%团队)
        player_share_c = target_budget * 0.75
        team_share_c = target_budget * 0.25
        models['个人责任模式'] = {
            '选手报名费(元/人)': round(player_share_c / self.total_players),
            '队伍建队费(元/队)': round(team_share_c / self.num_teams),
            '说明': '强调个人参与价值，减轻队长组织者的资金压力。'
        }

        return {
            '目标预算总额(元)': round(target_budget, 2),
            '收费方案': models
        }


if __name__ == '__main__':
    # 1. 创建一个赛事模型实例
    # (使用默认的12支队伍, 每队7人)
    lol_tournament = TournamentModel()

    # 2. 获取比赛和游戏局数的概要分析
    print("=" * 20 + " 赛事规模分析 " + "=" * 20)
    summary = lol_tournament.get_match_and_game_summary()
    for key, value in summary.items():
        print(f"{key}: {value}")

    print("\n" + "=" * 20 + " 赛事成本分析 " + "=" * 20)
    # 3. 获取成本分析
    costs = lol_tournament.get_cost_analysis()
    print(f"最低总成本: {costs['最低总成本']} 元")
    print(f"期望总成本: {round(costs['期望总成本'], 2)} 元")
    print(f"每局BO3成本: {costs['每局BO3成本']} 元")
    print(f"每局BO5成本: {costs['每局BO5成本']} 元")

    print("\n" + "=" * 20 + " 报名收费方案 " + "=" * 20)
    # 4. 获取收费方案 (使用默认的1.5倍预算阈值)
    fee_structures = lol_tournament.calculate_fee_models()
    print(f"目标预算总额: {fee_structures['目标预算总额']} 元")
    for model_name, details in fee_structures['收费方案'].items():
        print(f"\n--- {model_name} ---")
        print(f"  选手报名费: {details['选手报名费(元/人)']} 元/人")
        print(f"  队伍建队费: {details['队伍建队费(元/队)']} 元/队")
        print(f"  说明: {details['说明']}")

    # 你也可以使用自定义的预算乘数
    # custom_fees = lol_tournament.calculate_fee_models(cost_multiplier=2.0)
    # print("\n使用2.0倍阈值的收费方案:", custom_fees)