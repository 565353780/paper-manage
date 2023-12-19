# Paper Manage

## Search papers

### Zhiwang

search on url:

```bash
https://epub.cnki.net/kns/advsearch?dbcode=CDMD
```

and export with the format:

```bash
E-study
```

### Wanfang

search on url:

```bash
https://c.wanfangdata.com.cn/thesis
```

and export with the format:

```bash
NoteExpress
```

### ACM

search on url:

```bash
https://dl.acm.org/
```

and export with the format:

```bash
ACM Ref
```

### Save format

```bash
- Root
  |- Wanfang
      |- data1.txt
      |- data2.txt
      |- ...
  |- Zhiwang
      |- data1.txt
      |- data2.txt
      |- ...
  |- ACM
      |- data1.txt
      |- data2.txt
      |- ...
```

## Setup

```bash
conda create -n pm python=3.10
conda activate pm
./setup.sh
```

## Run

```bash
python demo.py
```

## Enjoy it~
