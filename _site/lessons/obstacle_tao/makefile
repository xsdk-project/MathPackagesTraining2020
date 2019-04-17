# Define the MFEM directories here
MFEM_DIR=/projects/ATPESC2018/FASTMath/spack/opt/spack/linux-rhel7-x86_64/gcc-4.8.5/mfem-develop-shrxlv7z4whbh2476qpdhuwtf6frzatv
PETSC_DIR=/projects/ATPESC2018/FASTMath/spack/opt/spack/linux-rhel7-x86_64/gcc-4.8.5/petsc-develop-xufshydc44bard4v7qinrl2nfetl7fcm

CONFIG_MK = $(MFEM_DIR)/share/mfem/config.mk
-include $(CONFIG_MK)
.SUFFIXES: .o .cpp .mk
.PHONY: all clean
.cpp.o:
	$(MFEM_CXX) $(MFEM_FLAGS) -c $<

all: obstacle

obstacle: obstacle.o
	$(MFEM_CXX) $(MFEM_FLAGS) $< -o $@ $(MFEM_LIBS) $(LDFLAGS)
clean:
	rm -f *.o *~ obstacle
	rm -rf *.dSYM *.TVD.*breakpoints obstacle_*
