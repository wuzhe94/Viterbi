# -*- coding: utf-8 -*-

# all possible observations
obs = ('obs1', 'obs2', 'obs3')

# all possible states
sts = ('sts1', 'sts2')

# the starting probability
start_prob = {
	'sts1': 0.3,
	'sts2': 0.7
}

# the transition probability
trans_prob = {
	'sts1': {'sts1': 0.6, 'sts2': 0.4},
	'sts2': {'sts1': 0.5, 'sts2': 0.5}
}

# the emission probability
emis_prob = {
	'sts1': {'obs1': 0.6, 'obs2': 0.3, 'obs3': 0.1},
	'sts2': {'obs1': 0.4, 'obs2': 0.5, 'obs3': 0.1}
}

# the current observations, as the default value of viterbi function
cur_obs = ['obs2', 'obs1', 'obs3']

def viterbi(observations = cur_obs):
	# confirm the input validity, if the input is not valid, raise IOE value
	try:
		for i in observations:
			if i in obs:
				pass
			else:
				raise IOError
	except IOError:
		print('Input Error!')
	# if the input is valid, then start the algorithm

	else:
		prob_lib = [{}]
		lst_path = {}
		cur_path = {}
		for i in range(len(observations)):
			if i == 0:
				for s in sts:
					prob_lib[i][s] = start_prob[s] * emis_prob[s][observations[i]]
					lst_path[s] = [s]
			else:
				prob_lib.append({})
				cur_path = {}
				for s in sts:
					(cur_max_prob, last_sts) = max([(prob_lib[i-1][s_last]
												  * trans_prob[s_last][s]
												  * emis_prob[s][observations[i]], s_last)
													for s_last in sts])
					prob_lib[i][s] = cur_max_prob
					cur_path[s] = lst_path[last_sts] + [s]
				lst_path = cur_path
		(final_max_prob, final_sta) = max([(prob_lib[len(observations)-1][s] ,s)
                                            for s in sts])

		print('The most possible state sequence is {},\nwith the probability of {}.'
			  .format(cur_path[final_sta],
					  final_max_prob))

# user can press the Enter key to use the built-in observations ['O2','O1','O3']
# Or input new observations separated by spaces
input_obs = input('If you want to use the original observation, press Enter key please.\n'
                      'Otherwise, enter your new observations separated by spaces:\n')

if input_obs == '':
	print('You are now using the default observations = [obs2, obs1, obs3].\n')
	viterbi()
else:
    input_obs = list(input_obs.split(' '))
    viterbi(input_obs)