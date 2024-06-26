import numpy as np
import abc
import util
from game import Agent, Action


class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """

    def get_action(self, game_state):
        """
        You do not need to change this method, but you're welcome to.

        get_action chooses among the best options according to the evaluation function.

        get_action takes a game_state and returns some Action.X for some X in the set {UP, DOWN, LEFT, RIGHT, STOP}
        """

        # Collect legal moves and successor states
        legal_moves = game_state.get_agent_legal_actions()

        # Choose one of the best actions
        scores = [self.evaluation_function(game_state, action) for action in legal_moves]
        best_score = max(scores)
        best_indices = [index for index in range(len(scores)) if scores[index] == best_score]
        chosen_index = np.random.choice(best_indices)  # Pick randomly among the best

        "Add more of your code here if you want to"

        return legal_moves[chosen_index]

    def evaluation_function(self, current_game_state, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (GameState.py) and returns a number, where higher numbers are better.

        """

        # Useful information you can extract from a GameState (game_state.py)

        successor_game_state = current_game_state.generate_successor(action=action)
        board = successor_game_state.board
        max_tile = successor_game_state.max_tile
        score = successor_game_state.score
        corners_coords = [(0, 0),(1,0),(2,0),(3,0)]
        return score + sum(
            [sum(board[(coord[0], y)] for y in range(4))
             for coord in corners_coords if board[coord] == max_tile])



def score_evaluation_function(current_game_state):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return current_game_state.score


class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinmaxAgent, AlphaBetaAgent & ExpectimaxAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evaluation_function='scoreEvaluationFunction', depth=2):
        self.evaluation_function = util.lookup(evaluation_function, globals())
        self.depth = depth




    @abc.abstractmethod
    def get_action(self, game_state):
        return




class MinmaxAgent(MultiAgentSearchAgent):

    def get_action(self, game_state):

        def maxmin_val(self, state, depth, agent_index):
            if depth == self.depth:
                return self.evaluation_function(state)

            if state == 0:
                alpha = float('-inf')
                for new_action in state.get_legal_actions(agent_index):
                    successor = state.generate_successor(agent_index, new_action)
                    alpha = max(alpha,
                                self.maxmin_val(successor, depth + 1, (agent_index + 1) % game_state.get_legal_actions(0)))
                return alpha
            else:
                beta = float('inf')
                for new_action in state.get_legal_actions(agent_index):
                    successor = state.generate_successor(agent_index, new_action)
                    beta = min(beta,
                               self.maxmin_val(successor, depth + 1, (agent_index + 1) % game_state.get_legal_actions(0)))
                return beta

        def check_top_action(self):
            flage = True
            max_value = -2
            top_action = 0
            for action in game_state.get_legal_actions(0):
                successor = game_state.generate_successor(0, action)
                value = maxmin_val(self, successor, 1, agent_index=0)
                if flage or value > max_value:
                    flage = False
                    max_value = maxmin_val(self, successor, 1, agent_index=0)
                    top_action = action
            return top_action

        return check_top_action(self)



    # def maxmin_val(self, state, depth, agent_index):
    #     if depth == self.depth:
    #         return self.evaluation_function(state)
    #
    #     agent = 0
    #
    #     if agent == 0:
    #         alpha = float('-inf')
    #         agent += 1
    #         for new_action in state.get_legal_actions(agent_index):
    #             successor = state.generate_successor(agent_index, new_action)
    #             alpha = max(alpha, self.maxmin_val(successor, depth + 0.5, (agent_index + 1) % 2))
    #         return alpha
    #     else:
    #         beta = float('inf')
    #         for new_action in state.get_legal_actions(agent_index):
    #             successor = state.generate_successor(agent_index, new_action)
    #             beta = min(beta, self.maxmin_val(successor, depth + 0.5, (agent_index + 1) % 2))
    #         return beta
    #
    # def get_action(self, game_state):
    #     """
    #     Returns the minimax action from the current gameState using self.depth
    #     and self.evaluationFunction.
    #     Here are some method calls that might be useful when implementing minimax.
    #     game_state.get_legal_actions(agent_index):
    #         Returns a list of legal actions for an agent
    #         agent_index=0 means our agent, the opponent is agent_index=1
    #     Action.STOP:
    #         The stop direction, which is always legal
    #     game_state.generate_successor(agent_index, action):
    #         Returns the successor game state after an agent takes an action
    #     """
    #     flage = True
    #     max_value = 0
    #     top_action = 0
    #     for action in game_state.get_legal_actions(0):
    #         successor = game_state.generate_successor(0, action)
    #         # half a step in depth to min
    #         value = self.maxmin_val(successor, 0.5, agent_index=1)
    #
    #         if flage or value > max_value:
    #             flage = False
    #             max_value = value
    #             top_action = action
    #     return top_action

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def get_action(self, game_state):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        """*** YOUR CODE HERE ***"""
        util.raiseNotDefined()



class ExpectimaxAgent(MultiAgentSearchAgent):
    """
    Your expectimax agent (question 4)
    """

    def get_action(self, game_state):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        The opponent should be modeled as choosing uniformly at random from their
        legal moves.
        """
        """*** YOUR CODE HERE ***"""
        util.raiseNotDefined()





def better_evaluation_function(current_game_state):
    """
    Your extreme 2048 evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviation
better = better_evaluation_function
