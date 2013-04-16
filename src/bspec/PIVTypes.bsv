import ClientServer::*;
import GetPut::*;

interface PIV;
  method ActionValue#(Displacements) getDisplacements;
  method Action putWindowReq(WindowReq req);
  method Action storeImage(Data x);
  method Action clearImage();
   // method ActionValue#(Data) cpuToHost;
   // method Action hostToCpu(Addr startpc);
   // interface MemInitIfc iMemInit;
endinterface

typedef 18 AddrSz;
typedef Bit#(AddrSz) Addr;

typedef 32 DataSz;
typedef Bit#(DataSz) Data;

typedef struct {
  PixelNdx ndx;
  WindowSize size;
} WindowReq deriving (Bits, Eq);

typedef Bit#(19) PixelNdx;

typedef Bit#(6) WindowSize;

typedef Bit#(4) Pixel;

typedef Int#(4) Displacement;

// typedef struct {
//   Displacement u;
//   Displacement v;
// } Displacements deriving (Bits, Eq);

typedef struct {
  Data u;
  Data v;
} Displacements deriving (Bits, Eq);

typedef Server#(
  WindowReq,
  Displacements
) WindowTracker;

typedef 480000 PIXELS_PER_IMAGE;

typedef 4 PIXELS_PER_LINE;
// typedef 4 PIXELS_PER_IMAGE;



typedef Bool ClearT;

