num_kernels = 0
kernel_dict = {}
timer_value = 600.0 #seconds

kernel = ''
kernel_name = ''
kernels = ('python', 'octave')
kernel_names = {'python':'python3', 'octave':'octave'}

import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)