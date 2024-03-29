import argparse
import os
import moxing
import main
def get_args():
    parser = argparse.ArgumentParser('two stream recurrent neural network')
    parser.add_argument('--data_url', type=str, default='./dataset')
    parser.add_argument('--train_url', type=str, default='./output')
    parser.add_argument('--base-dir', type=str, default='./code_test')
    parser.add_argument('--batch-size', type=int, default=16)
    parser.add_argument('--num-workers', type=int, default=0)
    parser.add_argument('--pretrained', type=bool, default=False)
    
    parser.add_argument('--cuda', type=bool, default=True)

    parser.add_argument('--lr', type=float, default=0.1)
    parser.add_argument('--weight-decay', type=float, default=5e-4)
    parser.add_argument('--momentum', type=float, default=0.9)

    parser.add_argument('--epochs', type=int, default=300)
    parser.add_argument('--print-interval', type=int, default=10)

    parser.add_argument('--temporal-size', type=int, default=100)
    parser.add_argument('--init_method'  )
    
    args = parser.parse_args()
    model_dir = "./output"
    data_dir = "./dataset"
    os.makedirs(model_dir)
    os.makedirs(data_dir)
    moxing.file.copy_parallel(args.data_url, data_dir) 
    main(args)
    moxing.file.copy_parallel(model_dir, args.train_url) 
    return args
