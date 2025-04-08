//=============================================================================
// This is an AXI Interconnect support two Master and one Slave
//=============================================================================

`timescale 1ns/1ns

module AXI_Interconnect
#(
    parameter DATA_WIDTH  = 32,
    parameter ADDR_WIDTH  = 32,
    parameter ID_WIDTH    = 1,
    parameter USER_WIDTH  = 4,
    parameter STRB_WIDTH  = (DATA_WIDTH/8)
)
(
	/********* System signals *********/
	input                       ACLK,
	input      	                ARESETn,
    /********** Master 0 **********/
    // AW Channel
	input      [ID_WIDTH-1:0]   m0_AWID,
    input	   [ADDR_WIDTH-1:0] m0_AWADDR,
    input      [7:0]            m0_AWLEN,
    input      [2:0]            m0_AWSIZE,
    input      [1:0]            m0_AWBURST,
    input                       m0_AWLOCK,
    input      [3:0]            m0_AWCACHE,
    input      [2:0]            m0_AWPROT,
    input      [3:0]            m0_AWQOS,
    input      [3:0]            m0_AWREGION,
    input      [USER_WIDTH-1:0] m0_AWUSER,
    input                       m0_AWVALID,
    output                      m0_AWREADY,
    // W Channel
    // input      [ID_WIDTH-1:0]   m0_WID,
    input      [DATA_WIDTH-1:0] m0_WDATA,
    input      [STRB_WIDTH-1:0] m0_WSTRB,
    input                       m0_WLAST,
    input      [USER_WIDTH-1:0] m0_WUSER,
    input                       m0_WVALID,
    output                      m0_WREADY,
    // B Channel
    output     [ID_WIDTH-1:0]	m0_BID,
	output     [1:0]	        m0_BRESP,
	output     [USER_WIDTH-1:0] m0_BUSER,
	output                      m0_BVALID,
    input                       m0_BREADY,
    // AR Channel
    input      [ID_WIDTH-1:0]   m0_ARID,
    input      [ADDR_WIDTH-1:0] m0_ARADDR,
    input      [7:0]            m0_ARLEN,
    input      [2:0]            m0_ARSIZE,
    input      [1:0]            m0_ARBURST,
    input                       m0_ARLOCK,
    input      [3:0]            m0_ARCACHE,
    input      [2:0]            m0_ARPROT,
    input      [3:0]            m0_ARQOS,
    input      [3:0]            m0_ARREGION,
    input      [USER_WIDTH-1:0] m0_ARUSER,
    input                       m0_ARVALID,
    output                      m0_ARREADY,
    // R Channel
    output     [ID_WIDTH-1:0]   m0_RID,
	output     [DATA_WIDTH-1:0] m0_RDATA,
	output     [1:0]	        m0_RRESP,
    output                      m0_RLAST,
	output     [USER_WIDTH-1:0]	m0_RUSER,
	output                      m0_RVALID,
    input                       m0_RREADY,
    /********** Master 1 **********/
    // AW Channel
    input      [ID_WIDTH-1:0]   m1_AWID,
    input	   [ADDR_WIDTH-1:0]	m1_AWADDR,
    input      [7:0]            m1_AWLEN,
    input      [2:0]            m1_AWSIZE,
    input      [1:0]            m1_AWBURST,
    input                       m1_AWLOCK,
    input      [3:0]            m1_AWCACHE,
    input      [2:0]            m1_AWPROT,
    input      [3:0]            m1_AWQOS,
    input      [3:0]            m1_AWREGION,
    input      [USER_WIDTH-1:0] m1_AWUSER,
    input                       m1_AWVALID,
    output                      m1_AWREADY,
    // W Channel
    // input      [ID_WIDTH-1:0]   m1_WID,
    input      [DATA_WIDTH-1:0] m1_WDATA,
    input      [STRB_WIDTH-1:0] m1_WSTRB,
    input                       m1_WLAST,
    input      [USER_WIDTH-1:0] m1_WUSER,
    input                       m1_WVALID,
    output                      m1_WREADY,
    // B Channel
    output     [ID_WIDTH-1:0]	m1_BID,
	output     [1:0]	        m1_BRESP,
	output     [USER_WIDTH-1:0] m1_BUSER,
	output                      m1_BVALID,
    input                       m1_BREADY,
    // AR Channel
    input      [ID_WIDTH-1:0]   m1_ARID,
    input      [ADDR_WIDTH-1:0] m1_ARADDR,
    input      [7:0]            m1_ARLEN,
    input      [2:0]            m1_ARSIZE,
    input      [1:0]            m1_ARBURST,
    input                       m1_ARLOCK,
    input      [3:0]            m1_ARCACHE,
    input      [2:0]            m1_ARPROT,
    input      [3:0]            m1_ARQOS,
    input      [3:0]            m1_ARREGION,
    input      [USER_WIDTH-1:0] m1_ARUSER,
    input                       m1_ARVALID,
    output                      m1_ARREADY,
    // R Channel
    output     [ID_WIDTH-1:0]   m1_RID,
	output     [DATA_WIDTH-1:0] m1_RDATA,
	output     [1:0]	        m1_RRESP,
    output                      m1_RLAST,
	output     [USER_WIDTH-1:0]	m1_RUSER,
	output                      m1_RVALID,
    input                       m1_RREADY,

    /********** Slave **********/
    // AW Channel
    output     [ID_WIDTH-1:0]   s_AWID,
    output     [ADDR_WIDTH-1:0]	s_AWADDR,
    output     [7:0]            s_AWLEN,
    output     [2:0]            s_AWSIZE,
    output     [1:0]            s_AWBURST,
    output                      s_AWLOCK,
    output     [3:0]            s_AWCACHE,
    output     [2:0]            s_AWPROT,
    output     [3:0]            s_AWQOS,
    output     [3:0]            s_AWREGION,
    output     [USER_WIDTH-1:0] s_AWUSER,
    output                      s_AWVALID,
    input	   	                s_AWREADY,
    // W Channel
    // output     [ID_WIDTH-1:0]   s_WID,
    output     [DATA_WIDTH-1:0] s_WDATA,
    output     [STRB_WIDTH-1:0] s_WSTRB,
    output                      s_WLAST,
    output     [USER_WIDTH-1:0] s_WUSER,
    output                      s_WVALID,
    input	  		            s_WREADY,
    // B Channel
	input	   [ID_WIDTH-1:0]	s_BID,
	input	   [1:0]	        s_BRESP,
	input	   [USER_WIDTH-1:0] s_BUSER,
	input	     		        s_BVALID,
    output                      s_BREADY,
    // AR Channel
    output     [ID_WIDTH-1:0]   s_ARID,    
    output     [ADDR_WIDTH-1:0] s_ARADDR,
    output     [7:0]            s_ARLEN,
    output     [2:0]            s_ARSIZE,
    output     [1:0]            s_ARBURST,
    output                      s_ARLOCK,
    output     [3:0]            s_ARCACHE,
    output     [2:0]            s_ARPROT,
    output     [3:0]            s_ARQOS,
    output     [3:0]            s_ARREGION,
    output     [USER_WIDTH-1:0] s_ARUSER,
    output                      s_ARVALID,
	input	  		            s_ARREADY,
    // R Channel
	input	   [ID_WIDTH-1:0]   s_RID,
	input	   [DATA_WIDTH-1:0] s_RDATA,
	input	   [1:0]	        s_RRESP,
	input	  		            s_RLAST,
	input	   [USER_WIDTH-1:0]	s_RUSER,
	input	 		            s_RVALID, 
    output                      s_RREADY
);


    //=========================================================
    wire  m0_wgrnt_w;
    wire  m1_wgrnt_w;
    wire  m0_wgrnt_r;
    wire  m1_wgrnt_r;

    //=========================================================
    AXI_Arbiter_W u_AXI_Arbiter_W(
        /********* System signals *********/
        .ACLK(ACLK),
        .ARESETn(ARESETn),
        /********** Master 0 **********/
        .m0_AWVALID(m0_AWVALID),
        .m0_WVALID(m0_WVALID),
        .m0_BREADY(m0_BREADY),
        /********** Master 1 **********/
        .m1_AWVALID(m1_AWVALID),
        .m1_WVALID(m1_WVALID),
        .m1_BREADY(m1_BREADY),
        /********** Slave **********/
        .s_AWREADY(s_AWREADY),
        .s_WREADY(s_WREADY),
        .s_BVALID(s_BVALID),
        
        .m0_wgrnt(m0_wgrnt_w),
        .m1_wgrnt(m1_wgrnt_w)
    );

    //=========================================================
    AXI_Arbiter_R u_AXI_Arbiter_R(
        /********* System signals *********/
        .ACLK(ACLK),
        .ARESETn(ARESETn),
        /********** Master 0 **********/
        .m0_ARVALID(m0_ARVALID),
        .m0_RREADY(m0_RREADY),
        /********** Master 1 **********/
        .m1_ARVALID(m1_ARVALID),
        .m1_RREADY(m1_RREADY),
        /********** Slave **********/
        .s_RVALID(s_RVALID),
        .s_RLAST(s_RLAST),
        
        .m0_rgrnt(m0_wgrnt_r),
        .m1_rgrnt(m1_wgrnt_r)
    );

    //=========================================================
    AXI_Master_Mux_W #(
        .DATA_WIDTH(DATA_WIDTH),
        .ADDR_WIDTH(ADDR_WIDTH),
        .ID_WIDTH(ID_WIDTH),
        .USER_WIDTH(USER_WIDTH),
        .STRB_WIDTH(STRB_WIDTH)
    )u_AXI_Master_Mux_W(
        /********** Master 0 **********/
        // AW Channel
        .m0_AWID(m0_AWID),
        .m0_AWADDR(m0_AWADDR),
        .m0_AWLEN(m0_AWLEN),
        .m0_AWSIZE(m0_AWSIZE),
        .m0_AWBURST(m0_AWBURST),
        .m0_AWLOCK(m0_AWLOCK),
        .m0_AWCACHE(m0_AWCACHE),
        .m0_AWPROT(m0_AWPROT),
        .m0_AWQOS(m0_AWQOS),
        .m0_AWREGION(m0_AWREGION),
        .m0_AWUSER(m0_AWUSER),
        .m0_AWVALID(m0_AWVALID),
        .m0_AWREADY(m0_AWREADY),
        // W Channel
        // .m0_WID(m0_WID),
        .m0_WDATA(m0_WDATA),
        .m0_WSTRB(m0_WSTRB),
        .m0_WLAST(m0_WLAST),
        .m0_WUSER(m0_WUSER),
        .m0_WVALID(m0_WVALID),
        .m0_WREADY(m0_WREADY),
        // B Channel
        .m0_BID(m0_BID),
        .m0_BRESP(m0_BRESP),
        .m0_BUSER(m0_BUSER),
        .m0_BVALID(m0_BVALID),
        .m0_BREADY(m0_BREADY),
        /********** Master 1 **********/
        // AW Channel
        .m1_AWID(m1_AWID),
        .m1_AWADDR(m1_AWADDR),
        .m1_AWLEN(m1_AWLEN),
        .m1_AWSIZE(m1_AWSIZE),
        .m1_AWBURST(m1_AWBURST),
        .m1_AWLOCK(m1_AWLOCK),
        .m1_AWCACHE(m1_AWCACHE),
        .m1_AWPROT(m1_AWPROT),
        .m1_AWQOS(m1_AWQOS),
        .m1_AWREGION(m1_AWREGION),
        .m1_AWUSER(m1_AWUSER),
        .m1_AWVALID(m1_AWVALID),
        .m1_AWREADY(m1_AWREADY),
        // W Channel
        // .m1_WID(m1_WID),
        .m1_WDATA(m1_WDATA),
        .m1_WSTRB(m1_WSTRB),
        .m1_WLAST(m1_WLAST),
        .m1_WUSER(m1_WUSER),
        .m1_WVALID(m1_WVALID),
        .m1_WREADY(m1_WREADY),
        // B Channel
        .m1_BID(m1_BID),
        .m1_BRESP(m1_BRESP),
        .m1_BUSER(m1_BUSER),
        .m1_BVALID(m1_BVALID),
        .m1_BREADY(m1_BREADY),
        /******** Slave ********/
        // AW Channel
        .s_AWID(s_AWID),
        .s_AWADDR(s_AWADDR),
        .s_AWLEN(s_AWLEN),
        .s_AWSIZE(s_AWSIZE),
        .s_AWBURST(s_AWBURST),
        .s_AWLOCK(s_AWLOCK),
        .s_AWCACHE(s_AWCACHE),
        .s_AWPROT(s_AWPROT),
        .s_AWQOS(s_AWQOS),
        .s_AWREGION(s_AWREGION),
        .s_AWUSER(s_AWUSER),
        .s_AWVALID(s_AWVALID),
        .s_AWREADY(s_AWREADY),
        // W Channel
        // .s_WID(s_WID),
        .s_WDATA(s_WDATA),
        .s_WSTRB(s_WSTRB),
        .s_WLAST(s_WLAST),
        .s_WUSER(s_WUSER),
        .s_WVALID(s_WVALID),
        .s_WREADY(s_WREADY),
        // B Channel
        .s_BID(s_BID),
        .s_BRESP(s_BRESP),
        .s_BUSER(s_BUSER),
        .s_BVALID(s_BVALID),
        .s_BREADY(s_BREADY),
        
        /******** input from Arbiter ********/
        .m0_wgrnt(m0_wgrnt_w),
        .m1_wgrnt(m1_wgrnt_w)
    );

    //=========================================================
    AXI_Master_Mux_R #(
        .DATA_WIDTH(DATA_WIDTH),
        .ADDR_WIDTH(ADDR_WIDTH),
        .ID_WIDTH(ID_WIDTH),
        .USER_WIDTH(USER_WIDTH)
    )u_AXI_Master_Mux_R(
        /********** Master 0 **********/
        // AR Channel
        .m0_ARID(m0_ARID),
        .m0_ARADDR(m0_ARADDR),
        .m0_ARLEN(m0_ARLEN),
        .m0_ARSIZE(m0_ARSIZE),
        .m0_ARBURST(m0_ARBURST),
        .m0_ARLOCK(m0_ARLOCK),
        .m0_ARCACHE(m0_ARCACHE),
        .m0_ARPROT(m0_ARPROT),
        .m0_ARQOS(m0_ARQOS),
        .m0_ARREGION(m0_ARREGION),
        .m0_ARUSER(m0_ARUSER),
        .m0_ARVALID(m0_ARVALID),
        .m0_ARREADY(m0_ARREADY),
        // R Channel
        .m0_RID(m0_RID),
        .m0_RDATA(m0_RDATA),
        .m0_RRESP(m0_RRESP),
        .m0_RLAST(m0_RLAST),
        .m0_RUSER(m0_RUSER),
        .m0_RVALID(m0_RVALID),
        .m0_RREADY(m0_RREADY),
        /********** Master 1 **********/
        // AR Channel
        .m1_ARID(m1_ARID),
        .m1_ARADDR(m1_ARADDR),
        .m1_ARLEN(m1_ARLEN),
        .m1_ARSIZE(m1_ARSIZE),
        .m1_ARBURST(m1_ARBURST),
        .m1_ARLOCK(m1_ARLOCK),
        .m1_ARCACHE(m1_ARCACHE),
        .m1_ARPROT(m1_ARPROT),
        .m1_ARQOS(m1_ARQOS),
        .m1_ARREGION(m1_ARREGION),
        .m1_ARUSER(m1_ARUSER),
        .m1_ARVALID(m1_ARVALID),
        .m1_ARREADY(m1_ARREADY),
        // R Channel
        .m1_RID(m1_RID),
        .m1_RDATA(m1_RDATA),
        .m1_RRESP(m1_RRESP),
        .m1_RLAST(m1_RLAST),
        .m1_RUSER(m1_RUSER),
        .m1_RVALID(m1_RVALID),
        .m1_RREADY(m1_RREADY),
        /******** Slave ********/
        // AR Channel
        .s_ARID(s_ARID),
        .s_ARADDR(s_ARADDR),
        .s_ARLEN(s_ARLEN),
        .s_ARSIZE(s_ARSIZE),
        .s_ARBURST(s_ARBURST),
        .s_ARLOCK(s_ARLOCK),
        .s_ARCACHE(s_ARCACHE),
        .s_ARPROT(s_ARPROT),
        .s_ARQOS(s_ARQOS),
        .s_ARREGION(s_ARREGION),
        .s_ARUSER(s_ARUSER),
        .s_ARVALID(s_ARVALID),
        .s_ARREADY(s_ARREADY),
        // R Channel
        .s_RID(s_RID),
        .s_RDATA(s_RDATA),
        .s_RRESP(s_RRESP),
        .s_RLAST(s_RLAST),
        .s_RUSER(s_RUSER),
        .s_RVALID(s_RVALID),
        .s_RREADY(s_RREADY),
        
        /******** input from Arbiter ********/
        .m0_rgrnt(m0_wgrnt_r),
        .m1_rgrnt(m1_wgrnt_r)
    );
    
endmodule