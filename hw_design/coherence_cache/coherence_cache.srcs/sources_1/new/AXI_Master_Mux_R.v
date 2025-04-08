//=============================================================================
// This Mux is used to select accessed signals between two Masters on Read Transactions
//=============================================================================

`timescale 1ns/1ns

module AXI_Master_Mux_R
#(
    parameter DATA_WIDTH  = 32,
    parameter ADDR_WIDTH  = 32,
    parameter ID_WIDTH    = 1,
    parameter USER_WIDTH  = 4
)
(
	
    /********** Master 0 **********/
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
    output reg                  m0_ARREADY,
    // R Channel
    output reg [ID_WIDTH-1:0]   m0_RID,
	output reg [DATA_WIDTH-1:0] m0_RDATA,
	output reg [1:0]	        m0_RRESP,
    output reg                  m0_RLAST,
	output reg [USER_WIDTH-1:0]	m0_RUSER,
	output reg                  m0_RVALID,
    input                       m0_RREADY,
    
    /********** Master 1 **********/
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
    output reg                  m1_ARREADY,
    // R Channel
    output reg [ID_WIDTH-1:0]   m1_RID,
	output reg [DATA_WIDTH-1:0] m1_RDATA,
	output reg [1:0]	        m1_RRESP,
    output reg                  m1_RLAST,
	output reg [USER_WIDTH-1:0]	m1_RUSER,
	output reg                  m1_RVALID,
    input                       m1_RREADY,
    
    /******** Slave ********/
    // AR Channel
    output reg [ID_WIDTH-1:0]   s_ARID,
    output reg [ADDR_WIDTH-1:0] s_ARADDR,
    output reg [7:0]            s_ARLEN,
    output reg [2:0]            s_ARSIZE,
    output reg [1:0]            s_ARBURST,
    output reg                  s_ARLOCK,
    output reg [3:0]            s_ARCACHE,
    output reg [2:0]            s_ARPROT,
    output reg [3:0]            s_ARQOS,
    output reg [3:0]            s_ARREGION,
    output reg [USER_WIDTH-1:0] s_ARUSER,
    output reg                  s_ARVALID,
    input                       s_ARREADY,
    // R Channel
    input	   [ID_WIDTH-1:0]   s_RID,
	input	   [DATA_WIDTH-1:0] s_RDATA,
	input	   [1:0]	        s_RRESP,
	input	  		            s_RLAST,
	input	   [USER_WIDTH-1:0]	s_RUSER,
    input                       s_RVALID,
    output reg                  s_RREADY,
    
    /******** input from Arbiter ********/
    input                       m0_rgrnt,
	input                       m1_rgrnt
);

    //---------------------------------------------------------
    // for Slave output
    always @(*) begin
        case({m0_rgrnt,m1_rgrnt})
            2'b10: begin
                // AR Channel
                s_ARID      =   m0_ARID;
                s_ARADDR    =   m0_ARADDR;
                s_ARLEN     =   m0_ARLEN;
                s_ARSIZE    =   m0_ARSIZE;
                s_ARBURST   =   m0_ARBURST;
                s_ARLOCK    =   m0_ARLOCK;
                s_ARCACHE   =   m0_ARCACHE;
                s_ARPROT    =   m0_ARPROT;
                s_ARQOS     =   m0_ARQOS;
                s_ARREGION  =   m0_ARREGION;
                s_ARUSER    =   m0_ARUSER;
                s_ARVALID   =   m0_ARVALID;
                // R Channel
                s_RREADY    =   m0_RREADY;
                
            end
            2'b01: begin
                // AR Channel
                s_ARID      =   m1_ARID;
                s_ARADDR    =   m1_ARADDR;
                s_ARLEN     =   m1_ARLEN;
                s_ARSIZE    =   m1_ARSIZE;
                s_ARBURST   =   m1_ARBURST;
                s_ARLOCK    =   m1_ARLOCK;
                s_ARCACHE   =   m1_ARCACHE;
                s_ARPROT    =   m1_ARPROT;
                s_ARQOS     =   m1_ARQOS;
                s_ARREGION  =   m1_ARREGION;
                s_ARUSER    =   m1_ARUSER;
                s_ARVALID   =   m1_ARVALID;
                // R Channel
                s_RREADY    =   m1_RREADY;
            end
            default: begin
                // AR Channel
                s_ARID      =   'b0;
                s_ARADDR    =   'b0;
                s_ARLEN     =   'b0;
                s_ARSIZE    =   'b0;
                s_ARBURST   =   'b0;
                s_ARLOCK    =   'b0;
                s_ARCACHE   =   'b0;
                s_ARPROT    =   'b0;
                s_ARQOS     =   'b0;
                s_ARREGION  =   'b0;
                s_ARUSER    =   'b0;
                s_ARVALID   =   'b0;
                // R Channel
                s_RREADY    =   'b0;
            end

        endcase
    end

    //---------------------------------------------------------
    //ARREADY
    always @(*) begin
        case({m0_rgrnt,m1_rgrnt})
            2'b10: begin
                // Master 0
                m0_ARREADY  = s_ARREADY;
                // Master 1
                m1_ARREADY  = 'b0;
            end
            2'b01: begin
                // Master 0
                m0_ARREADY  = 'b0;
                // Master 1
                m1_ARREADY  = s_ARREADY;
            end
            default: begin
                // Master 0
                m0_ARREADY  = 'b0;
                // Master 1
                m1_ARREADY  = 'b0;
            end
        endcase
    end

    //---------------------------------------------------------
    //RVALID
    always @(*) begin
        case({m0_rgrnt,m1_rgrnt})
            2'b10: begin
                // Master 0
                m0_RID     = s_RID  ;
                m0_RDATA   = s_RDATA;
                m0_RRESP   = s_RRESP;
                m0_RLAST   = s_RLAST;
                m0_RUSER   = s_RUSER;
                m0_RVALID  = s_RVALID;
                // Master 1
                m1_RID     = 'b0;
                m1_RDATA   = 'b0;
                m1_RRESP   = 'b0;
                m1_RLAST   = 'b0;
                m1_RUSER   = 'b0;
                m1_RVALID  = 'b0;
                m1_RVALID  = 'b0;
            end
            2'b01: begin
                // Master 0
                m0_RID     = 'b0;
                m0_RDATA   = 'b0;
                m0_RRESP   = 'b0;
                m0_RLAST   = 'b0;
                m0_RUSER   = 'b0;
                m0_RVALID  = 'b0;
                m0_RVALID  = 'b0;
                // Master 1
                m1_RID     = s_RID  ;
                m1_RDATA   = s_RDATA;
                m1_RRESP   = s_RRESP;
                m1_RLAST   = s_RLAST;
                m1_RUSER   = s_RUSER;
                m1_RVALID  = s_RVALID;
            end
            default: begin
                // Master 0
                m0_RID     = 'b0;
                m0_RDATA   = 'b0;
                m0_RRESP   = 'b0;
                m0_RLAST   = 'b0;
                m0_RUSER   = 'b0;
                m0_RVALID  = 'b0;
                m0_RVALID  = 'b0;
                m0_RVALID  = 'b0;
                // Master 1
                m1_RID     = 'b0;
                m1_RDATA   = 'b0;
                m1_RRESP   = 'b0;
                m1_RLAST   = 'b0;
                m1_RUSER   = 'b0;
                m1_RVALID  = 'b0;
                m1_RVALID  = 'b0;
            end
        endcase
    end

endmodule