function solution() {
    let ols = $('ol')
    let uls = $('ul')
    let depth = 0;
    for(let i = 0; i < ols.length; i++) {
      let parents = $(ols[i]).parents();
      let currdepth = 1
      for(let j = 0; j < parents.length; j++) {
        if(parents[j].tagName == 'OL' || parents[j].tagName == 'UL') {
          currdepth += 1
        }
      }
      if(depth < currdepth) {
        depth = currdepth;
      }
    }
    for(let i = 0; i < uls.length; i++) {
      let parents = $(uls[i]).parents();
      let currdepth = 1
      for(let j = 0; j < parents.length; j++) {
        if(parents[j].tagName == 'OL' || parents[j].tagName == 'UL') {
          currdepth += 1
        }
      }
      if(depth < currdepth) {
        depth = currdepth;
      }
    }
    return depth;
  }