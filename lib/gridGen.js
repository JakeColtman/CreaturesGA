var cell = {
  initCell: function(){
  this.visited=false;
  this.walls=[0,0,0,0];
  this.wallsDir={
    UP:[1,0,0,0],
    DOWN:[0,1,0,0],
    LEFT:[0,0,1,0],
    RIGHT:[0,0,0,1]
    };
  }
};

var dungeon = {
  initGrid: function(x,y,cellType){
    this.y=y;
    this.x=x;

    this.totalCells=x*y;
    this.cells=new Array();

      for(let i=0;i<y;i++){
        this.cells[i]=new Array();
          for(let j=0;j<x;j++){
            this.cells[i][j]=cellType;
          }
      }
  }
};
