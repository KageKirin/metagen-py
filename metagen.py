#! /usr/bin/env python3

import os, sys, re, codecs, site, pprint
site.addsitedir(os.path.dirname(__file__))
import argparse
from pathlib import Path
import colorama
colorama.init()
import xxhash
from string import Template

def generateMetaFile(filename, guid):
    tpl = Template(r"""fileFormatVersion: 2
guid: $guid
MonoImporter:
  externalObjects: {}
  serializedVersion: 2
  defaultReferences: []
  executionOrder: 0
  icon: {instanceID: 0}
  userData: 
  assetBundleName: 
  assetBundleVariant:
""")
    p = Path(filename)
    p = p.with_suffix(p.suffix + ".meta")
    p.write_text(tpl.substitute(guid=guid.hexdigest()))


def main(args):
    assert(args)
    assert(args.seed)
    assert(args.files)

    seed = xxhash.xxh64(args.seed)
    print(seed.hexdigest())

    for f in args.files:
        guid = xxhash.xxh128(f, seed=seed.intdigest())
        generateMetaFile(f, guid)

    

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Unity .meta file generator')
    parser.add_argument('-s', '--seed', help='seed string, e.g. package name', type=str, default=str(Path.cwd()))
    parser.add_argument('files', help='files to generate .meta files for', nargs='+')
    args = parser.parse_args()
    args.files = list(set(args.files))
    print(args)
    main(args)
