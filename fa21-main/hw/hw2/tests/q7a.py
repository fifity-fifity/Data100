OK_FORMAT = True
test = {   'name': 'q7a',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> len(draw_biased_state_sample(1000, "wisconsin")) == 3\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> __builtins__.sum(draw_biased_state_sample(1000, "michigan")) == 1000\nTrue', 'hidden': False, 'locked': False},
                                   {'code': '>>> q7_1 = draw_biased_state_sample(3000, "florida")\n>>> q7_1[0] > q7_1[2] and q7_1[1] > q7_1[2]\nTrue', 'hidden': False, 'locked': False},
                                   {   'code': '>>> assert len(biased_simulations) == 100000\n>>> assert __builtins__.sum([-1 < x < 1 for x in biased_simulations]) == len(biased_simulations)\n',
                                       'hidden': False,
                                       'locked': False},
                                   {'code': '>>> abs(np.mean(biased_simulations) + 0.003) <= 0.12\nTrue', 'hidden': False, 'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
