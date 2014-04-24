#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import logging
import os
from modules.topic_models.MalletLDA import BuildLDA

def TrainMallet( corpus_path, model_path, token_regex, num_topics, num_iters, is_quiet, force_overwrite ):
	logger = logging.getLogger( 'termite' )
	logger.addHandler( logging.StreamHandler() )
	logger.setLevel( logging.INFO if is_quiet else logging.DEBUG )
	
	logger.info( '--------------------------------------------------------------------------------' )
	logger.info( 'Training an LDA topic model using MALLET...' )
	logger.info( ' corpus_path = %s', corpus_path )
	logger.info( '  model_path = %s', model_path )
	logger.info( ' token_regex = %s', token_regex )
	logger.info( '      topics = %s', num_topics )
	logger.info( '       iters = %s', num_iters )
	logger.info( '--------------------------------------------------------------------------------' )
	
	if force_overwrite or not os.path.exists( model_path ):
		BuildLDA( corpus_path, model_path, tokenRegex = token_regex, numTopics = num_topics, numIters = num_iters )
	else:
		logger.info( '    Already exists: %s', model_path )

def main():
	parser = argparse.ArgumentParser( description = 'Train an LDA topic model using MALLET.' )
	parser.add_argument( 'corpus_path'  , type = str                              , help = 'Input corpus filename' )
	parser.add_argument( 'model_path'   , type = str                              , help = 'Output model path' )
	parser.add_argument( '--topics'     , type = int   , default = 20             , help = 'Number of topics' )
	parser.add_argument( '--iters'      , type = int   , default = 1000           , help = 'Number of iterations' )
	parser.add_argument( '--token-regex', type = str   , default = '\p{Alpha}{3,}', help = 'Tokenization', dest = 'token_regex' )
	parser.add_argument( '--quiet'      , const = True , default = False          , help = 'Show fewer debugging messages', action = 'store_const' )
	parser.add_argument( '--overwrite'  , const = True , default = False          , help = 'Overwrite any existing model', action = 'store_const' )
	args = parser.parse_args()
	TrainMallet( args.corpus_path, args.model_path, args.token_regex, args.topics, args.iters, args.quiet, args.overwrite )

if __name__ == '__main__':
	main()
