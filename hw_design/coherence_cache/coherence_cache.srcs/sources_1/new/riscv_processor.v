`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// this is riscv processor with AXI interface to D-Cache
//////////////////////////////////////////////////////////////////////////////////


module riscv_processor
#(
    parameter DATA_WIDTH  = 32,
    parameter ADDR_WIDTH  = 32,
    parameter ID_WIDTH    = 1,
    parameter USER_WIDTH  = 4,
    parameter STRB_WIDTH  = (DATA_WIDTH/8),
    parameter SHAREABLE_REGION_START = 32'h0002_0000, // start address of shareable region
    parameter SHAREABLE_REGION_END   = 32'h0003_FFFF  // end address of shareable region
)
(
    // system signals
    output                      ACLK,
    output                      ARESETn,
    
    // Interface connect with D-Cache
    // D-Cache enable
    output                      d_CACHE_EN,
    
    // AXI5 Interface
    // AW Channel
    output   [ID_WIDTH-1:0]     d_AWID,
    output   [ADDR_WIDTH-1:0]   d_AWADDR,
    output   [7:0]              d_AWLEN,
    output   [2:0]              d_AWSIZE,
    output   [1:0]              d_AWBURST,
    output                      d_AWLOCK,
    output   [3:0]              d_AWCACHE,
    output   [2:0]              d_AWPROT,
    output   [3:0]              d_AWQOS,
    output   [3:0]              d_AWREGION,
    output   [USER_WIDTH-1:0]   d_AWUSER,
    output   [1:0]              d_AWDOMAIN,
    output                      d_AWVALID,
    input                       d_AWREADY,
    
    // W Channel
    output   [DATA_WIDTH-1:0]   d_WDATA,
    output   [STRB_WIDTH-1:0]   d_WSTRB, 
    output                      d_WLAST,
    output   [USER_WIDTH-1:0]   d_WUSER,
    output                      d_WVALID,
    input                       d_WREADY,
    
    // B Channel
    input  [ID_WIDTH-1:0]       d_BID,
    input  [1:0]                d_BRESP,
    input  [USER_WIDTH-1:0]     d_BUSER,
    input                       d_BVALID,
    output                      d_BREADY,
   
    // AR Channe
    output   [ID_WIDTH-1:0]     d_ARID,
    output   [ADDR_WIDTH-1:0]   d_ARADDR,
    output   [7:0]              d_ARLEN,
    output   [2:0]              d_ARSIZE,
    output   [1:0]              d_ARBURST,
    output                      d_ARLOCK,
    output   [3:0]              d_ARCACHE,
    output   [2:0]              d_ARPROT,
    output   [3:0]              d_ARQOS,
    output   [3:0]              d_ARREGION,
    output   [USER_WIDTH-1:0]   d_ARUSER,
    output   [1:0]              d_ARDOMAIN,
    output                      d_ARVALID,
    input                       d_ARREADY,
    
    // R Channel
    input  [ID_WIDTH-1:0]       d_RID,
    input  [DATA_WIDTH-1:0]     d_RDATA,
    input  [1:0]                d_RRESP,
    input                       d_RLAST,
    input  [USER_WIDTH-1:0]	    d_RUSER,
    input                       d_RVALID,
    output                      d_RREADY
);


endmodule
