from argparse import ArgumentParser
import py_stats as st




def _get_args():
  parser = ArgumentParser( prog='stats' )
  parser.add_argument( 'filename' )
  parser.add_argument( '-a', '--analysis-type', default='hyp' )
  parser.add_argument( '-d', '--data-type', default='solutions' )
  return parser.parse_args()


def _main( args ):
  t, s = st.read_solution_and_time_data( args.filename )
  if args.analysis_type == 'hyp':
    x = t if args.data_type == 'time' else s
    greater = st.two_rel_samples_analysis( x[:, 0], x[:, 1] )
    if greater == 0: print( f'A = B' )
    if greater == 1: print( f'A > B' )
    if greater == 2: print( f'A < B' )
    return
  if args.analysis_type == 'ci':
    x = t[:, 0] if args.data_type == 'time' else s[:, 0] / s[:, 1]
    if st.is_normal_dist( x ): low, hi = st.confidence_interval( x )
    else: low, hi = st.bootstrap( x )
    print( f'CI: {low} - {hi}' )
    return


if __name__ == '__main__': _main( _get_args() )
