#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import logging
import os
from modules.topic_models.TreeTM import BuildLDA, RefineLDA

def TrainTreeTM( corpus_path, model_path, token_regex, num_topics, num_iters, is_quiet, force_overwrite, resume_training ):
	logger = logging.getLogger( 'termite' )
	logger.addHandler( logging.StreamHandler() )
	logger.setLevel( logging.INFO if is_quiet else logging.DEBUG )
	
	if force_overwrite or not os.path.exists( model_path ):
		logger.info( '--------------------------------------------------------------------------------' )
		logger.info( 'Training a new interactive topic model...' )
		logger.info( '      corpus = %s', corpus_path )
		logger.info( '       model = %s', model_path )
		logger.info( ' token_regex = %s', token_regex )
		logger.info( '      topics = %s', num_topics )
		logger.info( '       iters = %s', num_iters )
		logger.info( '--------------------------------------------------------------------------------' )
		BuildLDA( corpus_path, model_path, tokenRegex = token_regex, numTopics = num_topics, numIters = num_iters )
	else:
		if resume_training:
			logger.info( '--------------------------------------------------------------------------------' )
			logger.info( 'Training an existing interactive topic model...' )
			logger.info( '       model = %s', model_path )
			logger.info( '       iters = %s', num_iters )
			logger.info( '--------------------------------------------------------------------------------' )
			RefineLDA( model_path, numIters = num_iters )
		else:
			logger.info( '--------------------------------------------------------------------------------' )
			logger.info( 'Training an interactive topic model...' )
			logger.info( '--------------------------------------------------------------------------------' )
			logger.info( '    Already exists: %s', model_path )

def main():
	parser = argparse.ArgumentParser( description = 'Train an interactive topic model.' )
	parser.add_argument( 'corpus_path'  , type = str                              , help = 'Input corpus filename' )
	parser.add_argument( 'model_path'   , type = str                              , help = 'Output model path' )
	parser.add_argument( '--topics'     , type = int   , default = 20             , help = 'Number of topics' )
	parser.add_argument( '--iters'      , type = int   , default = 1000           , help = 'Number of iterations' )
	parser.add_argument( '--token-regex', type = str   , default = '\p{Alpha}{3,}', help = 'Tokenization', dest = 'token_regex' )
	parser.add_argument( '--quiet'      , const = True , default = False          , help = 'Show fewer debugging messages', action = 'store_const' )
	parser.add_argument( '--overwrite'  , const = True , default = False          , help = 'Overwrite any existing model', action = 'store_const' )
	parser.add_argument( '--resume'     , const = True , default = False          , help = 'Resume training', action = 'store_const' )
	args = parser.parse_args()
	TrainTreeTM( args.corpus_path, args.model_path, args.token_regex, args.topics, args.iters, args.quiet, args.overwrite, args.resume )

if __name__ == '__main__':
	main()
